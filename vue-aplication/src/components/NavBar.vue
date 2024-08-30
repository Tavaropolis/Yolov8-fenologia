<script setup lang="ts">
import { RouterLink } from 'vue-router'

</script>

<template>
    <nav>
        <div class="nav-bar">
            <img src="../assets/folha.png" alt="Folha de árvore" class="nav-logo">
            <ul>
                <li><RouterLink to="/">Home</RouterLink></li>
                <li><RouterLink to="/sobre">Sobre</RouterLink></li>
            </ul>
        </div>
    </nav>
</template>

<style scoped>
.nav-bar {
    width: 100vw;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background: var(--menu-color);
}

.nav-logo {
    width: 40px;
    height: 40px;
}

ul {
    width: 12vw;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    list-style: none;
}

ul li a {
    cursor: pointer;
    color: var( --text-color);
    text-decoration: none;
}
</style>