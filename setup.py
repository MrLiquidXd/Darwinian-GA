import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='Darwinian',
    version='0.0.4.1',
    description='“Darwinian” - это модуль Python, который реализует Дарвиновский Генетический Алгоритм (GA) для задач оптимизации. GA симулирует процесс естественного отбора, где наиболее приспособленные особи выбираются для воспроизводства, чтобы произвести потомство следующего поколения.',
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    url="https://github.com/MrLiquidXd/Darwinian-GA",
    author="Vinner Arseniy",
    author_email="mrliquidxd@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    install_requires = [],
    )