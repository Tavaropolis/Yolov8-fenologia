# Yolov8 aplicado a fenologia
Projeto de conclusão do curso de Análise e Desenvolvimento de Sistemas pelo Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) - Campus Capivari. O projeto consiste em aplicar Inteligência Artificial e Visão Computacional as áreas de Fenologia e Botânica. 

A aplicação consiste em um front-end em Vue.js 3, que recebe uma imagem de uma árvore, e faz uma chamada de API a um modelo de IA treinado dentro da plataforma [Roboflow](https://roboflow.com/) que reconhece a copa da árvore na imagem e devolve os pontos de marcação. Após isso, o front-end faz uma requisição ao back-end, formado por uma aplicação Flask, que recebe as área da copa, analisa os pixels da imagem evia biblioteca opencv, e consegue inferir a intensidade de presença foliar.  

## Para rodar localmente

### Aplicação Vue
Acessar a pasta da aplicação front-end com o comando 
```
cd .\vue-aplication\   
```
Instalar os módulos e rodar localmente
```javascript
npm install
```
```javascript
npm run dev
```

### Aplicação Python/Flask
Acessar a pasta da aplicação back-end com o comando 
```
cd .\python-aplication\
```
Criar um ambiente virtual(venv)
```
python -m venv venv
```
Ativar o ambiente virtual (no Windows)
```
venv\Scripts\activate
```
Dentro do ambiente virtual, instalar as dependências
```python
pip uninstall -r requirements.txt
```
Desativar o ambiente virtual
```python
deactivate
```
Rodar o Flask localmente
```python
flask run
```
