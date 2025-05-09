# Vuetify component v-range-slider - usage

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
      <v-range-slider v-bind="props"></v-range-slider>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="disabled" label="Disabled"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-range-slider'
  const model = ref('default')
  const options = ['vertical']
  const disabled = ref(false)
  const props = computed(() => {
    return {
      direction: model.value === 'vertical' ? 'vertical' : undefined,
      disabled: disabled.value || undefined,
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

# Vuetify component v-range-slider - prop min and max

Example code

```vue
<template>
  <v-range-slider
    v-model="range"
    :max="10"
    :min="-10"
    :step="1"
    class="align-center"
    hide-details
  >
    <template v-slot:prepend>
      <v-text-field
        v-model="range[0]"
        density="compact"
        style="width: 70px"
        type="number"
        variant="outlined"
        hide-details
        single-line
      ></v-text-field>
    </template>
    <template v-slot:append>
      <v-text-field
        v-model="range[1]"
        density="compact"
        style="width: 70px"
        type="number"
        variant="outlined"
        hide-details
        single-line
      ></v-text-field>
    </template>
  </v-range-slider>
</template>

<script setup>
  import { ref } from 'vue'

  const range = ref([-5, 5])
</script>

<script>
  export default {
    data () {
      return {
        range: [-5, 5],
      }
    },
  }
</script>

```

# Vuetify component v-range-slider - prop strict

Example code

```vue
<template>
  <v-card>
    <v-card-text>
      <v-range-slider
        v-model="value"
        strict
      ></v-range-slider>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref([20, 40])
</script>

<script>
  export default {
    data () {
      return {
        value: [20, 40],
      }
    },
  }
</script>

```

# Vuetify component v-range-slider - prop disabled

Example code

```vue
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-range-slider
          v-model="value"
          label="Disabled"
          disabled
        ></v-range-slider>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref([30, 60])
</script>

<script>
  export default {
    data () {
      return {
        value: [30, 60],
      }
    },
  }
</script>

```

# Vuetify component v-range-slider - slot thumb label

Example code

```vue
<template>
  <v-row>
    <v-col class="pa-12">
      <v-range-slider
        :model-value="[0, 1]"
        :step="1"
        :ticks="seasons"
        max="3"
        min="0"
        show-ticks="always"
        thumb-label="always"
        tick-size="4"
      >
        <template v-slot:thumb-label="{ modelValue }">
          <v-icon :icon="season(modelValue)" theme="dark"></v-icon>
        </template>
      </v-range-slider>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const seasons = ref({
    0: 'Winter',
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
  })
  const icons = ref([
    'mdi-snowflake',
    'mdi-leaf',
    'mdi-fire',
    'mdi-water',
  ])
  function season (val) {
    return icons.value[val]
  }
</script>

<script>
  export default {
    data: () => ({
      seasons: {
        0: 'Winter',
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
      },
      icons: [
        'mdi-snowflake',
        'mdi-leaf',
        'mdi-fire',
        'mdi-water',
      ],
    }),

    methods: {
      season (val) {
        return this.icons[val]
      },
    },
  }
</script>

```

# Vuetify component v-range-slider - prop vertical

Example code

```vue
<template>
  <v-range-slider
    v-model="value"
    direction="vertical"
  ></v-range-slider>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref([20, 40])
</script>

<script>
  export default {
    data () {
      return {
        value: [20, 40],
      }
    },
  }
</script>

```

# Vuetify component v-range-slider - prop step

Example code

```vue
<template>
  <v-range-slider
    v-model="value"
    step="10"
    thumb-label="always"
  ></v-range-slider>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref([20, 40])
</script>

<script>
  export default {
    data () {
      return {
        value: [20, 40],
      }
    },
  }
</script>

```
