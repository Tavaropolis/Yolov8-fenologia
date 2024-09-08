<script setup>
import NavBar from "../components/NavBar.vue";
import References from "../components/References.vue";
import AboutApp from "../components/AboutApp.vue";
import AboutAI from "../components/AboutAI.vue";
import AboutFeno from '../components/AboutFeno.vue';
import AboutRCNN from "../components/AboutRCNN.vue"

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
            <AboutAI/>
        </section>
        <section class="buffer" id="topic3">
            <AboutFeno/>
        </section>
        <section class="buffer" id="topic4">
            <AboutRCNN/>
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