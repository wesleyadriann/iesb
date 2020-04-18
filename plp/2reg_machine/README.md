2Reg Machine
============

Desenvolver um interpretador para a Máquina 2REG, conforme a especificação da linguagem na 03ª Lista de Exercícios.

## Rodando

#### Docker (recomendado)
Na pasta code execute
```bash
docker build . -t <container_tag>
docker run -it <container_tag> sh
python3 . '<file_path>'
```
<file_path> é o arquivo padrão que será lido, o padrão é 2r_program.txt  
<container_tag> é o nome que o container terá

#### Python
Na pasta code execute
```bash
python3 .
```
ou
```bash
python3 . '<file_path>'
```
<file_path> é o arquivo padrão que será lido, o padrão é 2r_program.txt  
