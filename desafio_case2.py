import json
from openai import OpenAI

# Inicializa o client OpenAI se possível
client = None
usa_api = False
try:
    client = OpenAI()
    usa_api = True
except Exception:
    print("OpenAI client. Usando feedback simulado.")

def carregar_candidatos(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

criterios = {
    "skills_minimas": ["Python", "SQL"],
    "cultura_minima": ["Flexibilidade"],
    "experiencia_minima": 2
}

def filtrar_candidatos(lista, criterios):
    aprovados = []
    reprovados = []
    for c in lista:
        tem_skills = all(skill in c["skills"] for skill in criterios["skills_minimas"])
        tem_cultura = any(cult in c["cultura"] for cult in criterios["cultura_minima"])
        tem_exp = c["experiencia_anos"] >= criterios["experiencia_minima"]

        if tem_skills and tem_cultura and tem_exp:
            aprovados.append(c)
        else:
            reprovados.append(c)
    return aprovados, reprovados

def gerar_feedback_api(nome, motivos):
    prompt = f"""
Você é um recrutador respeitoso e construtivo. Gere um feedback educado para o candidato {nome} que não foi aprovado por estes motivos: {motivos}. Seja encorajador e sugira pontos para melhoria.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def gerar_feedback_simulado(nome, motivos):
    return (
        f"Caro(a) {nome}, infelizmente você não atendeu a todos os critérios necessários para esta vaga "
        f"por estes motivos: {motivos}. Continue se aprimorando e tente novamente em futuras oportunidades!"
    )

def gerar_feedback(nome, motivos):
    if usa_api:
        try:
            return gerar_feedback_api(nome, motivos)
        except Exception as e:
            print(f"Erro na API OpenAI: {e}. Usando feedback simulado.")
            return gerar_feedback_simulado(nome, motivos)
    else:
        return gerar_feedback_simulado(nome, motivos)

def rankear_candidatos(aprovados):
    return sorted(aprovados, key=lambda c: (c["experiencia_anos"], len(c["skills"])), reverse=True)

def mostrar_metricas(total, aprovados, reprovados):
    print("\n=== Métricas ===")
    print(f"Total de candidatos: {total}")
    print(f"Aprovados: {len(aprovados)} ({len(aprovados)/total*100:.1f}%)")
    print(f"Reprovados: {len(reprovados)} ({len(reprovados)/total*100:.1f}%)")

def main():
    arquivo = input("Digite o nome do arquivo JSON com os candidatos: ").strip()
    try:
        candidatos = carregar_candidatos(arquivo)
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return

    aprovados, reprovados = filtrar_candidatos(candidatos, criterios)
    aprovados_rank = rankear_candidatos(aprovados)

    print("\n=== Candidatos aprovados (ranking) ===")
    for i, c in enumerate(aprovados_rank, 1):
        print(f"{i}. {c['nome']} - Experiência: {c['experiencia_anos']} anos, Skills: {', '.join(c['skills'])}")

    print("\n=== Feedback para candidatos reprovados ===")
    for r in reprovados:
        motivos = []
        if not all(skill in r["skills"] for skill in criterios["skills_minimas"]):
            motivos.append("não possui as skills técnicas mínimas")
        if not any(cult in r["cultura"] for cult in criterios["cultura_minima"]):
            motivos.append("não demonstra alinhamento cultural")
        if r["experiencia_anos"] < criterios["experiencia_minima"]:
            motivos.append("não possui experiência mínima requerida")
        motivo_str = ", ".join(motivos)
        feedback = gerar_feedback(r["nome"], motivo_str)
        print(f"\n{r['nome']}:\n{feedback}")

    mostrar_metricas(len(candidatos), aprovados, reprovados)

if __name__ == "__main__":
    main()
