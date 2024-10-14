<script setup>
const props = defineProps({
    msg: String
})
</script>
<template>
    <div class="modal-container">
        <div class="error-modal">
            {{ props.msg }}
        </div>
    </div>
</template>
<style scoped>
.modal-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.error-modal {
    width: 45vw;
    background-color: var(--color-error-modal);
    text-align: center;
    font-weight: bold;
    border-radius: 5px;
}
</style>