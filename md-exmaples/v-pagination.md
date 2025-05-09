# Vuetify component v-pagination - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div>
      <v-pagination
        v-bind="props"
      ></v-pagination>
    </div>

    <template v-slot:configuration>
      <v-slider v-model="length" label="Length" max="20" min="1"></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-pagination'
  const model = ref('default')
  const length = ref(4)
  const options = []

  const props = computed(() => {
    return {
      length: length.value,
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<v-pagination${propsToString(props.value)}>${slots.value}</v-pagination>`
  })
</script>

```

# Vuetify component v-pagination - prop total visible

Example code

```vue
<template>
  <div class="text-center">
    <v-pagination
      v-model="page"
      :length="15"
      :total-visible="7"
    ></v-pagination>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const page = ref(1)
</script>

<script>
  export default {
    data () {
      return {
        page: 1,
      }
    },
  }
</script>

```

# Vuetify component v-pagination - prop rounded

Example code

```vue
<template>
  <div class="text-center">
    <v-pagination
      v-model="page"
      :length="4"
      rounded="circle"
    ></v-pagination>

    <v-pagination
      v-model="page"
      :length="4"
      rounded="0"
    ></v-pagination>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const page = ref(1)
</script>

<script>
  export default {
    data () {
      return {
        page: 1,
      }
    },
  }
</script>

```

# Vuetify component v-pagination - prop length

Example code

```vue
<template>
  <div class="text-center">
    <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              :length="15"
              class="my-4"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const page = ref(1)
</script>

<script>
  export default {
    data () {
      return {
        page: 1,
      }
    },
  }
</script>

```

# Vuetify component v-pagination - prop icons

Example code

```vue
<template>
  <div class="text-center">
    <v-pagination
      v-model="page"
      :length="4"
      next-icon="mdi-menu-right"
      prev-icon="mdi-menu-left"
    ></v-pagination>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const page = ref(1)
</script>

<script>
  export default {
    data () {
      return {
        page: 1,
      }
    },
  }
</script>

```

# Vuetify component v-pagination - prop disabled

Example code

```vue
<template>
  <div class="text-center">
    <v-pagination
      :length="3"
      disabled
    ></v-pagination>
  </div>
</template>

```
