from pathlib import Path
base = Path("C:/Users/Ailton J/Downloads/BFD_BACK_END_PYTHON-main (1)/BFD_BACK_END_PYTHON-main/lista estruturas de controle")

for i in range(1, 15):
    file = base / f"exercicio_{i}.py"
    file.write_text(f"# Exercicio {i}\n")
