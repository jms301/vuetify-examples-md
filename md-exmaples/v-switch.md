# Vuetify component v-switch - usage

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
      <v-switch v-bind="props"></v-switch>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="indeterminate" label="Indeterminate"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-switch'
  const model = ref('default')
  const indeterminate = ref(false)
  const options = ['inset']
  const props = computed(() => {
    return {
      label: 'Switch',
      inset: model.value === 'inset' || undefined,
      indeterminate: indeterminate.value || undefined,
    }
  })

  watch(model, () => indeterminate.value = false)

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-switch - prop custom values

Example code

```vue
<template>
  <v-switch
    v-model="model"
    :label="`Switch: ${model}`"
    false-value="no"
    true-value="yes"
    hide-details
  ></v-switch>
</template>

<script setup>
  import { ref } from 'vue'

  const model = ref('no')
</script>

<script>
  export default {
    data: () => ({
      model: 'no',
    }),
  }
</script>

```

# Vuetify component v-switch - prop states

Example code

```vue
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="6">
        <v-switch
          :model-value="true"
          color="primary"
          label="on"
        ></v-switch>
      </v-col>
      <v-col cols="6">
        <v-switch
          :model-value="false"
          color="primary"
          label="off"
        ></v-switch>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="6">
        <v-switch
          :model-value="true"
          color="primary"
          label="on disabled"
          disabled
        ></v-switch>
      </v-col>
      <v-col cols="6">
        <v-switch
          :model-value="false"
          color="primary"
          label="off disabled"
          disabled
        ></v-switch>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="6">
        <v-switch
          :model-value="true"
          label="on loading"
          loading="warning"
        ></v-switch>
      </v-col>
      <v-col cols="6">
        <v-switch
          :model-value="false"
          label="off loading"
          loading="warning"
        ></v-switch>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-switch - prop flat

Example code

```vue
<template>
  <v-switch
    v-model="model"
    :label="`Switch: ${model.toString()}`"
    flat
    hide-details
  ></v-switch>
</template>

<script setup>
  import { ref } from 'vue'

  const model = ref(true)
</script>

<script>
  export default {
    data () {
      return {
        model: true,
      }
    },
  }
</script>

```

# Vuetify component v-switch - prop inset

Example code

```vue
<template>
  <v-switch
    v-model="model"
    :label="`Switch: ${model.toString()}`"
    hide-details
    inset
  ></v-switch>
</template>

<script setup>
  import { ref } from 'vue'

  const model = ref(true)
</script>

<script>
  export default {
    data () {
      return {
        model: true,
      }
    },
  }
</script>

```

# Vuetify component v-switch - prop model as array

Example code

```vue
<template>
  <v-container fluid>
    <p>{{ people }}</p>
    <v-switch
      v-model="people"
      color="primary"
      label="John"
      value="John"
      hide-details
    ></v-switch>
    <v-switch
      v-model="people"
      color="primary"
      label="Jacob"
      value="Jacob"
      hide-details
    ></v-switch>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const people = ref(['John'])
</script>

<script>
  export default {
    data () {
      return {
        people: ['John'],
      }
    },
  }
</script>

```

# Vuetify component v-switch - prop colors

Example code

```vue
<template>
  <v-card flat>
    <v-card-text>
      <v-container fluid>
        <v-row>
          <v-col
            cols="12"
            md="4"
            sm="4"
          >
            <v-switch
              v-model="ex11"
              color="red"
              label="red"
              value="red"
              hide-details
            ></v-switch>
            <v-switch
              v-model="ex11"
              color="red-darken-3"
              label="red-darken-3"
              value="red-darken-3"
              hide-details
            ></v-switch>
          </v-col>
          <v-col
            cols="12"
            md="4"
            sm="4"
          >
            <v-switch
              v-model="ex11"
              color="indigo"
              label="indigo"
              value="indigo"
              hide-details
            ></v-switch>
            <v-switch
              v-model="ex11"
              color="indigo-darken-3"
              label="indigo-darken-3"
              value="indigo-darken-3"
              hide-details
            ></v-switch>
          </v-col>
          <v-col
            cols="12"
            md="4"
            sm="4"
          >
            <v-switch
              v-model="ex11"
              color="orange"
              label="orange"
              value="orange"
              hide-details
            ></v-switch>
            <v-switch
              v-model="ex11"
              color="orange-darken-3"
              label="orange-darken-3"
              value="orange-darken-3"
              hide-details
            ></v-switch>
          </v-col>
        </v-row>

        <v-row class="mt-12">
          <v-col
            cols="12"
            md="4"
            sm="4"
          >
            <v-switch
              v-model="ex11"
              color="primary"
              label="primary"
              value="primary"
              hide-details
            ></v-switch>
            <v-switch
              v-model="ex11"
              color="secondary"
              label="secondary"
              value="secondary"
              hide-details
            ></v-switch>
          </v-col>
          <v-col
            cols="12"
            md="4"
            sm="4"
          >
            <v-switch
              v-model="ex11"
              color="success"
              label="success"
              value="success"
              hide-details
            ></v-switch>
            <v-switch
              v-model="ex11"
              color="info"
              label="info"
              value="info"
              hide-details
            ></v-switch>
          </v-col>
          <v-col
            cols="12"
            md="4"
            sm="4"
          >
            <v-switch
              v-model="ex11"
              color="warning"
              label="warning"
              value="warning"
              hide-details
            ></v-switch>
            <v-switch
              v-model="ex11"
              color="error"
              label="error"
              value="error"
              hide-details
            ></v-switch>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script setup>
  const ex11 = ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red-darken-3', 'indigo-darken-3', 'orange-darken-3']
</script>

<script>
  export default {
    data () {
      return {
        ex11: ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red-darken-3', 'indigo-darken-3', 'orange-darken-3'],
      }
    },
  }
</script>

```

# Vuetify component v-switch - slot label

Example code

```vue
<template>
  <v-switch v-model="switchMe">
    <template v-slot:label>
      Turn on the progress:
      <v-progress-circular
        :indeterminate="switchMe"
        class="ms-2"
        size="24"
      ></v-progress-circular>
    </template>
  </v-switch>
</template>

<script setup>
  import { ref } from 'vue'

  const switchMe = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        switchMe: false,
      }
    },
  }
</script>

```
