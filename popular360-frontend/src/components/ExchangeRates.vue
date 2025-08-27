<template>
  <div class="min-h-screen flex flex-col">
    <img src="../assets/logo.svg" alt="Logo" class="h-16 mx-auto my-4" />

    <section class="relative h-[500px] flex items-center justify-center text-center">
      <img src="../assets/blog_home_info.png" alt="Hero Background" class="absolute inset-0 w-full h-full object-cover z-0" />
      <div class="relative z-10 text-white px-6">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">Bienvenido a Popular360</h1>
        <p class="text-lg md:text-xl mb-8">Tus tasas de interés y tipo de cambio en tiempo real</p>
        <button class="bg-white text-[#0f62fe] font-bold px-12 py-3 rounded-lg shadow hover:bg-gray-200 transition">
          Explorar
        </button>
      </div>
      <div class="absolute inset-0 bg-black opacity-30 z-0"></div>
    </section>

    <section class="py-16 px-6 max-w-6xl mx-auto">
       <h2 class="text-3xl font-bold mb-8 text-center">Tipo de Cambio</h2> 
       <div v-if="interest" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 ml-0 md:ml-40"> 
        <div v-for="m in interest.monedas.moneda" :key="m.descripcion" class="p-6 bg-white rounded-lg shadow transition" > 
          <h3 class="text-xl font-bold">{{ m.descripcion }}</h3> 
          <p class="text-gray-700">Compra: <span class="font-semibold">{{ m.compra }}</span></p> 
          <p class="text-gray-700">Venta: <span class="font-semibold">{{ m.venta }}</span></p> 
        </div> 
      </div> 
      <p v-else class="text-center text-gray-500">Cargando tipo de cambio...</p> 
    </section>

    <!-- Sección tasas de interés -->
    <section class="py-16 px-6 bg-gray-50">
      <h2 class="text-3xl font-bold mb-8 text-center">Tasas de Interés</h2>
      <div v-if="exchange" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div
          v-for="(tasa, producto) in exchange.tasasint.tasaprestamos"
          :key="producto"
          class="p-6 bg-white rounded-lg shadow transition"
        >
          <h3 class="text-lg font-bold">{{ producto }}</h3>
          <p class="text-gray-700">Tasa: <span class="font-semibold">{{ tasa }}%</span></p>
        </div>
      </div>
      <p v-else class="text-center text-gray-500">Cargando tasas de interés...</p>
    </section>

     <!-- Sección de cards informativas / features -->
    <section class="py-16 px-6 max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold mb-8 text-center">Servicios Destacados</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-md transition flex flex-col items-center">
            <div class="rounded-full w-15 h-15 bg-gray-200 flex items-center justify-center">
              <CreditCard class="h-40 w-8"/>
            </div>
          <h3 class="text-xl font-bold mb-2 mt-4">Préstamos</h3>
          <p class="text-gray-700 text-center">Consulta las tasas más competitivas para tus préstamos personales y empresariales.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md transition flex flex-col items-center">
            <div class="rounded-full w-15 h-15 bg-gray-200 flex items-center justify-center">
              <PiggyBank class="h-40 w-8"/>
            </div>
          <h3 class="text-xl font-bold mb-2 mt-4">Ahorros</h3>
          <p class="text-gray-700 text-center">Cuentas de ahorro con interés atractivo y seguridad total.</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md transition flex flex-col items-center">
            <div class="rounded-full w-15 h-15 bg-gray-200 flex items-center justify-center">
              <RefreshCw class="h-40 w-8"/>
            </div>
          <h3 class="text-xl font-bold mb-2 mt-4">Tipo de Cambio</h3>
          <p class="text-gray-700 text-center">Monitorea en tiempo real los tipos de cambio de divisas.</p>
        </div>
      </div>
    </section>

    <footer class="relative mt-auto h-[200px]">
      <img src="../assets/footer_backgnd_two.png" alt="footer image" class="absolute inset-0 w-full h-full object-cover z-0" />
      <div class="relative z-10 max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center h-full text-white">
        <p>&copy; 2025 Popular360. Todos los derechos reservados.</p>
        <div class="flex space-x-4 mt-4 md:mt-0">
          <a href="https://github.com/AngelEmilioAquino" target="_blank">
            <Github class="w-6 h-6 text-white hover:text-sky-600 transition" />
          </a>
          <a href="https://www.linkedin.com/in/angel-emilio-aquino/" target="_blank">
            <Linkedin class="w-6 h-6 text-white hover:text-sky-600 transition" />
          </a>
          <a href="mailto:angelemilioaquino6@gmail.com" target="_blank">
            <Mail class="w-6 h-6 text-white hover:text-sky-600 transition" />
          </a>
        </div>

        <div class="flex space-x-4 mt-4 md:mt-0">
          <a class="hover:underline">Privacidad</a>
          <a class="hover:underline">Términos</a>
          <a class="hover:underline">Contacto</a>
        </div>
      </div>
      <div class="absolute inset-0 bg-black opacity-30 z-0"></div>
    </footer>

  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { getExchangeRates, getInterestRates } from '../services/api';
import { CreditCard, PiggyBank, RefreshCw } from 'lucide-vue-next'
import { Linkedin, Github, Mail } from "lucide-vue-next"

const exchange = ref(null);
const interest = ref(null);

onMounted(async () => {
  try {
    exchange.value = await getExchangeRates();
    interest.value = await getInterestRates();
  } catch (e) {
    console.error("Error cargando datos:", e);
  }
});
</script>
