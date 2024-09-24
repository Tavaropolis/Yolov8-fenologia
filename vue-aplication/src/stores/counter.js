import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})

export const imgStore = defineStore('imgResult', () => {
  const imgResult = ref({
    base64Img: "",
    confidence: 0,
    leaf_index: 0
  });

  return { imgResult }
})