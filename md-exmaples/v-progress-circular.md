# Vuetify component v-progress-circular - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="text-center">
      <v-progress-circular v-bind="props"></v-progress-circular>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="color"
        :items="['primary', 'blue-lighten-3', 'error', 'dark-blue']"
        label="Color"
        clearable
      ></v-select>

      <v-slider
        v-model="size"
        label="Size"
        max="128"
        min="32"
        step="1"
      ></v-slider>

      <v-slider
        v-model="width"
        label="Width"
        max="12"
        min="4"
        step="1"
      ></v-slider>

      <v-checkbox v-model="indeterminate" label="Indeterminate"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-progress-circular'
  const model = ref('default')
  const color = ref()
  const indeterminate = ref(false)
  const size = ref()
  const width = ref()
  const options = []
  const props = computed(() => {
    return {
      color: color.value || undefined,
      indeterminate: indeterminate.value || undefined,
      'model-value': !indeterminate.value ? '20' : undefined,
      size: size.value !== 32 ? size.value : undefined,
      width: width.value !== 4 ? width.value : undefined,
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

# Vuetify component v-progress-circular - prop indeterminate

Example code

```vue
<template>
  <div class="text-center">
    <v-progress-circular
      color="primary"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      color="red"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      color="purple"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      color="green"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      color="amber"
      indeterminate
    ></v-progress-circular>
  </div>
</template>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>

```

# Vuetify component v-progress-circular - prop size and width

Example code

```vue
<template>
  <div class="text-center">
    <v-progress-circular
      :size="50"
      color="primary"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      :width="3"
      color="red"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      :size="70"
      :width="7"
      color="purple"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      :width="3"
      color="green"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      :size="50"
      color="amber"
      indeterminate
    ></v-progress-circular>
  </div>
</template>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>

```

# Vuetify component v-progress-circular - prop color

Example code

```vue
<template>
  <div class="text-center">
    <v-progress-circular
      color="blue-grey"
      model-value="100"
    ></v-progress-circular>

    <v-progress-circular
      color="deep-orange-lighten-2"
      model-value="80"
    ></v-progress-circular>

    <v-progress-circular
      color="brown"
      model-value="60"
    ></v-progress-circular>

    <v-progress-circular
      color="lime"
      model-value="40"
    ></v-progress-circular>

    <v-progress-circular
      color="indigo-darken-2"
      model-value="20"
    ></v-progress-circular>
  </div>
</template>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>

```

# Vuetify component v-progress-circular - prop rotate

Example code

```vue
<template>
  <div class="text-center">
    <v-progress-circular
      :model-value="value"
      :rotate="360"
      :size="100"
      :width="15"
      color="teal"
    >
      {{ value }}
    </v-progress-circular>

    <v-progress-circular
      :model-value="value"
      :rotate="-90"
      :size="100"
      :width="15"
      color="primary"
    >
      {{ value }}
    </v-progress-circular>

    <v-progress-circular
      :model-value="value"
      :rotate="90"
      :size="100"
      :width="15"
      color="red"
    >
      {{ value }}
    </v-progress-circular>

    <v-progress-circular
      :model-value="value"
      :rotate="180"
      :size="100"
      :width="15"
      color="pink"
    >
      {{ value }}
    </v-progress-circular>
  </div>
</template>

<script setup>
  import { onBeforeUnmount, onMounted, ref } from 'vue'

  const value = ref(0)

  let interval = -1
  onMounted(() => {
    interval = setInterval(() => {
      if (value.value === 100) {
        return (value.value = 0)
      }
      value.value += 10
    }, 1000)
  })
  onBeforeUnmount(() => {
    clearInterval(interval)
  })
</script>

<script>
  export default {
    data () {
      return {
        interval: {},
        value: 0,
      }
    },
    beforeUnmount () {
      clearInterval(this.interval)
    },
    mounted () {
      this.interval = setInterval(() => {
        if (this.value === 100) {
          return (this.value = 0)
        }
        this.value += 10
      }, 1000)
    },
  }
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>

```

# Vuetify component v-progress-circular - prop slot default

Example code

```vue
<template>
  <div class="text-center">
    <v-progress-circular :model-value="value" :rotate="360" :size="100" :width="15" color="teal">
      <template v-slot:default> {{ value }} % </template>
    </v-progress-circular>
  </div>
</template>

<script setup>
  import { onBeforeUnmount, onMounted, ref } from 'vue'

  const value = ref(0)

  let interval = -1
  onMounted(() => {
    interval = setInterval(() => {
      if (value.value === 100) {
        return (value.value = 0)
      }
      value.value += 10
    }, 1000)
  })
  onBeforeUnmount(() => {
    clearInterval(interval)
  })
</script>

<script>
  export default {
    data () {
      return {
        interval: -1,
        value: 0,
      }
    },
    mounted () {
      this.interval = setInterval(() => {
        if (this.value === 100) {
          return (this.value = 0)
        }
        this.value += 10
      }, 1000)
    },
    beforeUnmount () {
      clearInterval(this.interval)
    },
  }
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>

```
