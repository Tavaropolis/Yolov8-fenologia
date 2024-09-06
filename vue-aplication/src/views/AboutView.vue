<script setup>
import NavBar from "../components/NavBar.vue";
import References from "../components/References.vue";
import AboutApp from "../components/AboutApp.vue";
import AboutAI from "../components/AboutAI.vue";
import AboutFeno from '../components/AboutFeno.vue';

</script>

<template>
    <NavBar/>
    <h1>Sobre o projeto</h1>
    <summary>
        <ul>
            <li><a href="#topic1">Como funciona a aplicação?</a></li>
            <li><a href="#topic2">O que é IA?</a></li>
            <li><a href="#topic3">O que é fenologia?</a></li>
            <li><a href="#topic4">O que é R-CNN?</a></li>
            <li><a href="#topic5">Referências Bibliográficas</a></li>
        </ul>
    </summary>
    <main>
        <section class="buffer" id="topic1">
            <AboutApp/>
        </section>
        <div class="parallax" id="img-1"></div>
        <section class="buffer" id="topic2">
            <h2>O que é IA?</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident ab dignissimos pariatur neque ipsum corporis numquam voluptatem ex. Cupiditate neque earum quisquam similique ducimus architecto cumque autem, quia nemo minus.</p>
        </section>
        <section class="buffer" id="topic3">
            <AboutFeno/>
        </section>
        <section class="buffer" id="topic4">
            <h2>O que é R-CNN?</h2>
            <p>&emsp;CNN (Convolutional Neural Networks) é uma forma de se obter a classificação de uma imagem, através de redes neurais profundas, o deeplearning. O CNN se utiliza de "kernels" formados por fórmulas matemáticas, que analisam uma determinada matriz de pixels por vez, até passar por toda a imagem. Esses kernels tem a capacidade de identificar certas características da imagem, por exemplo, um pode identidicar pontas, ou kernel pode identificar blur, e assim por diante. Após o resultado obtido o CNN classifica a imagem conforme o treinamento aplicado. Por exemplo: alimenta-se o CNN com várias imagens classificadas como sendo um cachorro, o CNN aprende as características que formam esse tipo de imagem, e ao ser alimentado com outra imagem, ele saberá classificar se é um cachorro ou não.</p>
            <p>&emsp; Este modelo entretanto tem suas limitações, sendo relativamente desafiador identificar quando a mais de um mesmo objeto na imagem e classifica-la. Para resolver esses desafios é utilizado a abordagem R-CNN. A principal diferença desta abordagem é que há uma classificação de zonas de interesse por padrões na imagem, antes da aplicação dos kernels.</p>
        </section>
        <div class="parallax" id="img-2"></div>
        <section class="buffer" id="topic5">
            <References/>
        </section>
    </main>
</template>

<style scoped>
.buffer {
    text-align: justify;
    max-width: 100%;
}

.parallax{
    min-height: 50vh;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    /*  this is where the magic happens:  */
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
}

#img-1{
    background-image: url("../assets/flowerthree.jpg");
}

#img-2{
    background-image: url("../assets/jungleplants.jpg");
}

a {
    color: var( --color-text);
    text-decoration: none;
}

a:hover {
    cursor: pointer;
    color: var( --color-text-focus);
    text-decoration: none;
}

p {
    padding: 10px;
}

</style>