# Vuetify component v-sparkline - usage

Example code

```vue
<template>
  <v-sparkline
    :auto-line-width="autoLineWidth"
    :fill="fill"
    :gradient="gradient"
    :gradient-direction="gradientDirection"
    :line-width="width"
    :model-value="value"
    :padding="padding"
    :smooth="radius || false"
    :stroke-linecap="lineCap"
    :type="type"
    auto-draw
  ></v-sparkline>
</template>

<script>
  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]

  export default {
    data: () => ({
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: 'round',
      gradient: gradients[5],
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      gradientDirection: 'top',
      gradients,
      fill: false,
      type: 'trend',
      autoLineWidth: false,
    }),
  }
</script>

```

# Vuetify component v-sparkline - misc dashboard card

Example code

```vue
<template>
  <v-card
    class="mt-8 mx-auto overflow-visible"
    max-width="400"
  >
    <v-sheet
      class="v-sheet--offset mx-auto"
      color="cyan"
      elevation="12"
      max-width="calc(100% - 32px)"
      rounded="lg"
    >
      <v-sparkline
        :labels="labels"
        :model-value="value"
        color="white"
        line-width="2"
        padding="16"
      ></v-sparkline>
    </v-sheet>

    <v-card-text class="pt-0">
      <div class="text-h6 font-weight-light mb-2">
        User Registrations
      </div>
      <div class="subheading font-weight-light text-grey">
        Last Campaign Performance
      </div>
      <v-divider class="my-2"></v-divider>
      <v-icon
        class="me-2"
        size="small"
      >
        mdi-clock
      </v-icon>
      <span class="text-caption text-grey font-weight-light">last registration 26 minutes ago</span>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const labels = ref([
    '12am',
    '3am',
    '6am',
    '9am',
    '12pm',
    '3pm',
    '6pm',
    '9pm',
  ])
  const value = ref([
    200,
    675,
    410,
    390,
    310,
    460,
    250,
    240,
  ])
</script>

<script>
  export default {
    data: () => ({
      labels: [
        '12am',
        '3am',
        '6am',
        '9am',
        '12pm',
        '3pm',
        '6pm',
        '9pm',
      ],
      value: [
        200,
        675,
        410,
        390,
        310,
        460,
        250,
        240,
      ],
    }),
  }
</script>

<style>
  .v-sheet--offset {
    top: -24px;
    position: relative;
  }
</style>

```

# Vuetify component v-sparkline - prop fill

Example code

```vue
<template>
  <v-container fluid>
    <v-sparkline
      :fill="fill"
      :gradient="selectedGradient"
      :line-width="lineWidth"
      :model-value="value"
      :padding="padding"
      :smooth="smooth"
      auto-draw
    ></v-sparkline>

    <v-divider></v-divider>

    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-row
          align="center"
          class="fill-height"
        >
          <v-item-group
            v-model="selectedGradient"
            mandatory
          >
            <v-row
              class="pt-6 pl-6"
            >
              <v-item
                v-for="(gradient, i) in gradients"
                :key="i"
                v-slot="{ active, toggle }"
                :value="gradient"
              >
                <v-card
                  :style="{
                    background: gradient.length > 1
                      ? `linear-gradient(0deg, ${gradient})`
                      : gradient[0],
                    border: '2px solid',
                    borderColor: active ? '#222' : 'white'
                  }"
                  class="me-2"
                  height="30"
                  width="30"
                  @click="toggle"
                ></v-card>
              </v-item>
            </v-row>
          </v-item-group>
        </v-row>
      </v-col>
    </v-row>

    <v-row
      class="mt-5"
    >
      <v-col
        cols="2"
      >
        Filled
      </v-col>
      <v-col
        cols="3"
      >
        <v-switch
          v-model="fill"
          class="switch"
        ></v-switch>
      </v-col>
      <v-col
        cols="3"
      >
        Line width
      </v-col>
      <v-col
        cols="3"
      >
        <v-slider
          v-model="lineWidth"
          max="10"
          min="0.1"
          step="0.1"
          thumb-label
        ></v-slider>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        cols="2"
      >
        Smooth
      </v-col>
      <v-col
        cols="3"
      >
        <v-switch
          v-model="smooth"
          class="switch"
        ></v-switch>
      </v-col>
      <v-col
        cols="3"
      >
        Padding
      </v-col>
      <v-col
        cols="3"
      >
        <v-slider
          v-model="padding"
          cols="3"
          max="25"
          min="0"
          thumb-label
        ></v-slider>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]
  const fill = ref(true)
  const selectedGradient = ref(gradients[4])
  const padding = ref(8)
  const smooth = ref(true)
  const value = ref([0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0])
  const lineWidth = ref(2)
</script>

<script>
  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]

  export default {
    data: () => ({
      fill: true,
      selectedGradient: gradients[4],
      gradients,
      padding: 8,
      smooth: true,
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      lineWidth: 2,
    }),
  }
</script>

<style scoped>
.switch {
  position: relative;
  top: -12px;
}
</style>

```

# Vuetify component v-sparkline - misc heart rate

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="surface-light"
    max-width="600"
  >
    <template v-slot:prepend>
      <v-icon
        :color="checking ? 'red lighten-2' : 'indigo-lighten-2'"
        class="me-8"
        icon="mdi-heart-pulse"
        size="64"
        @click="takePulse"
      ></v-icon>
    </template>

    <template v-slot:title>
      <div class="text-caption text-grey text-uppercase">
        Heart rate
      </div>

      <span
        class="text-h3 font-weight-black"
        v-text="avg || '—'"
      ></span>
      <strong v-if="avg">BPM</strong>
    </template>

    <template v-slot:append>
      <v-btn
        class="align-self-start"
        icon="mdi-arrow-right-thick"
        size="34"
        variant="text"
      ></v-btn>
    </template>

    <v-sheet color="transparent">
      <v-sparkline
        :key="String(avg)"
        :gradient="['#f72047', '#ffd200', '#1feaea']"
        :line-width="3"
        :model-value="heartbeats"
        :smooth="16"
        stroke-linecap="round"
        auto-draw
      ></v-sparkline>
    </v-sheet>
  </v-card>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const exhale = ms => new Promise(resolve => setTimeout(resolve, ms))
  const checking = ref(false)
  const heartbeats = ref([])
  const avg = computed(() => {
    const sum = heartbeats.value.reduce((acc, cur) => acc + cur, 0)
    const length = heartbeats.value.length
    if (!sum && !length) return 0
    return Math.ceil(sum / length)
  })
  function heartbeat () {
    return Math.ceil(Math.random() * (120 - 80) + 80)
  }
  async function takePulse (inhale = true) {
    checking.value = true
    inhale && await exhale(1000)
    heartbeats.value = Array.from({ length: 20 }, heartbeat)
    checking.value = false
  }
  takePulse(false)
</script>

<script>
  const exhale = ms =>
    new Promise(resolve => setTimeout(resolve, ms))

  export default {
    data: () => ({
      checking: false,
      heartbeats: [],
    }),

    computed: {
      avg () {
        const sum = this.heartbeats.reduce((acc, cur) => acc + cur, 0)
        const length = this.heartbeats.length

        if (!sum && !length) return 0

        return Math.ceil(sum / length)
      },
    },

    created () {
      this.takePulse(false)
    },

    methods: {
      heartbeat () {
        return Math.ceil(Math.random() * (120 - 80) + 80)
      },
      async takePulse (inhale = true) {
        this.checking = true

        inhale && await exhale(1000)

        this.heartbeats = Array.from({ length: 20 }, this.heartbeat)

        this.checking = false
      },
    },
  }
</script>

```

# Vuetify component v-sparkline - misc custom labels

Example code

```vue
<template>
  <v-card
    class="mx-auto text-center"
    color="green"
    max-width="600"
    dark
  >
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :model-value="value"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
        >
          <template v-slot:label="item">
            ${{ item.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Sales Last 24h
      </div>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="justify-center">
      <v-btn
        variant="text"
        block
      >
        Go to Report
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref([
    423,
    446,
    675,
    510,
    590,
    610,
    760,
  ])
</script>

<script>
  export default {
    data: () => ({
      value: [
        423,
        446,
        675,
        510,
        590,
        610,
        760,
      ],
    }),
  }
</script>

```
