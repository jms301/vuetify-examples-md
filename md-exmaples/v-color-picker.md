# Vuetify component v-color-picker - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="d-flex justify-center">
      <v-color-picker v-bind="props"></v-color-picker>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="hideCanvas" label="Hide canvas"></v-checkbox>

      <v-checkbox v-model="hideInputs" label="Hide inputs"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-color-picker'
  const model = ref('default')
  const options = ['Disabled', 'Show swatches']
  const hideCanvas = ref()
  const hideInputs = ref()
  const props = computed(() => {
    return {
      disabled: model.value === 'Disabled' ? true : undefined,
      'hide-canvas': hideCanvas.value || undefined,
      'hide-inputs': hideInputs.value || undefined,
      'show-swatches': model.value === 'Show swatches' ? true : undefined,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-color-picker - prop elevation

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-color-picker
      v-model="picker"
      elevation="0"
    ></v-color-picker>

    <v-color-picker
      v-model="picker"
      elevation="15"
    ></v-color-picker>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        picker: null,
      }
    },
  }
</script>

```

# Vuetify component v-color-picker - prop mode

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-color-picker
      v-model="color"
      :modes="['rgba']"
    ></v-color-picker>

    <div class="d-flex flex-column">
      <v-color-picker
        v-model="color"
        v-model:mode="mode"
      ></v-color-picker>
      <v-select
        v-model="mode"
        :items="modes"
        style="max-width: 300px"
      ></v-select>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const color = ref('#ff00ff')
  const mode = ref('hsla')
  const modes = ref(['hsla', 'rgba', 'hexa'])
</script>

<script>
  export default {
    data: () => ({
      color: '#ff00ff',
      mode: 'hsla',
      modes: ['hsla', 'rgba', 'hexa'],
    }),
  }
</script>

```

# Vuetify component v-color-picker - prop model

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        md="4"
      >
        <v-btn class="my-4" block @click="color = null">null</v-btn>
        <v-btn class="my-4" block @click="color = '#ff00ff'">hex</v-btn>
        <v-btn class="my-4" block @click="color = '#ff00ffff'">hexa</v-btn>
        <v-btn class="my-4" block @click="color = { r: 255, g: 0, b: 255, a: 1 }">rgba</v-btn>
        <v-btn class="my-4" block @click="color = { h: 300, s: 1, l: 0.5, a: 1 }">hsla</v-btn>
        <v-btn class="my-4" block @click="color = { h: 300, s: 1, v: 1, a: 1 }">hsva</v-btn>
      </v-col>
      <v-col
        class="d-flex justify-center"
      >
        <v-color-picker v-model="color"></v-color-picker>
      </v-col>
      <v-col
        cols="12"
        md="4"
      >
        <v-sheet
          class="pa-4"
        >
          <pre>{{ color }}</pre>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const color = ref(null)
</script>

<script>
  export default {
    data: () => ({
      color: null,
    }),
  }
</script>

```

# Vuetify component v-color-picker - prop canvas

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-color-picker
      v-model="c1"
      hide-canvas
      hide-sliders
    ></v-color-picker>

    <v-color-picker
      v-model="c2"
      hide-inputs
      show-swatches
    ></v-color-picker>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const c1 = ref('#ff00ff')
  const c2 = ref('#00ff00')
</script>

<script>

  export default {
    data: () => ({
      c1: '#ff00ff',
      c2: '#00ff00',
    }),
  }
</script>

```

# Vuetify component v-color-picker - prop swatches

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-color-picker
      class="ma-2"
      swatches-max-height="400px"
      show-swatches
    ></v-color-picker>
    <v-color-picker
      :swatches="swatches"
      class="ma-2"
      show-swatches
    ></v-color-picker>
  </div>
</template>

<script setup>
  const swatches = [
    ['#FF0000', '#AA0000', '#550000'],
    ['#FFFF00', '#AAAA00', '#555500'],
    ['#00FF00', '#00AA00', '#005500'],
    ['#00FFFF', '#00AAAA', '#005555'],
    ['#0000FF', '#0000AA', '#000055'],
  ]
</script>

<script>
  export default {
    data: () => ({
      swatches: [
        ['#FF0000', '#AA0000', '#550000'],
        ['#FFFF00', '#AAAA00', '#555500'],
        ['#00FF00', '#00AA00', '#005500'],
        ['#00FFFF', '#00AAAA', '#005555'],
        ['#0000FF', '#0000AA', '#000055'],
      ],
    }),
  }
</script>

```
