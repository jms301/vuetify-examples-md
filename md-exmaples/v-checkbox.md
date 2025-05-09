# Vuetify component v-checkbox - usage

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
      <v-checkbox v-bind="props" hide-details></v-checkbox>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-checkbox'
  const model = ref('default')
  const options = []
  const props = computed(() => {
    return {
      label: 'Checkbox',
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

# Vuetify component v-checkbox - prop model as boolean

Example code

```vue
<template>
  <v-container fluid>
    <v-checkbox
      v-model="checkbox1"
      :label="`Checkbox 1: ${checkbox1.toString()}`"
    ></v-checkbox>
    <v-checkbox
      v-model="checkbox2"
      :label="`Checkbox 2: ${checkbox2.toString()}`"
    ></v-checkbox>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const checkbox1 = ref(true)
  const checkbox2 = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        checkbox1: true,
        checkbox2: false,
      }
    },
  }
</script>

```

# Vuetify component v-checkbox - prop states

Example code

```vue
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        on
      </v-col>
      <v-col cols="4">
        off
      </v-col>
      <v-col cols="4">
        indeterminate
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="4">
        <v-checkbox
          :model-value="true"
        ></v-checkbox>
      </v-col>
      <v-col cols="4">
        <v-checkbox :model-value="false"></v-checkbox>
      </v-col>
      <v-col cols="4">
        <v-checkbox
          indeterminate
        ></v-checkbox>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="4">
        on disabled
      </v-col>
      <v-col cols="4">
        off disabled
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="4">
        <v-checkbox
          :model-value="true"
          disabled
        ></v-checkbox>
      </v-col>
      <v-col cols="4">
        <v-checkbox
          :model-value="false"
          disabled
        ></v-checkbox>
      </v-col>
      <v-col cols="4">
        <v-checkbox
          disabled
          indeterminate
        ></v-checkbox>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-checkbox - misc inline textfield

Example code

```vue
<template>
  <v-card>
    <v-card-text>
      <div class="d-flex pa-4">
        <v-checkbox-btn
          v-model="includeFiles"
          class="pe-2"
        ></v-checkbox-btn>
        <v-text-field
          label="Include files"
          hide-details
        ></v-text-field>
      </div>
      <div class="d-flex pa-4">
        <v-checkbox-btn
          v-model="enabled"
          class="pe-2"
        ></v-checkbox-btn>
        <v-text-field
          :disabled="!enabled"
          label="I only work if you check the box"
          hide-details
        ></v-text-field>
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const includeFiles = ref(true)
  const enabled = ref(false)
</script>

<script>
  export default {
    data: () => ({
      includeFiles: true,
      enabled: false,
    }),
  }
</script>

```

# Vuetify component v-checkbox - prop model as array

Example code

```vue
<template>
  <v-container fluid>
    <p>{{ selected }}</p>
    <v-checkbox
      v-model="selected"
      label="John"
      value="John"
    ></v-checkbox>
    <v-checkbox
      v-model="selected"
      label="Jacob"
      value="Jacob"
    ></v-checkbox>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const selected = ref(['John'])
</script>

<script>
  export default {
    data () {
      return {
        selected: ['John'],
      }
    },
  }
</script>

```

# Vuetify component v-checkbox - prop colors

Example code

```vue
<template>
  <div>
    <v-container fluid>
      <v-row>
        <v-col
          cols="12"
          md="4"
          sm="4"
        >
          <v-checkbox
            v-model="ex4"
            color="red"
            label="red"
            value="red"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="ex4"
            color="red-darken-3"
            label="red-darken-3"
            value="red-darken-3"
            hide-details
          ></v-checkbox>
        </v-col>
        <v-col
          cols="12"
          md="4"
          sm="4"
        >
          <v-checkbox
            v-model="ex4"
            color="indigo"
            label="indigo"
            value="indigo"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="ex4"
            color="indigo-darken-3"
            label="indigo-darken-3"
            value="indigo-darken-3"
            hide-details
          ></v-checkbox>
        </v-col>
        <v-col
          cols="12"
          md="4"
          sm="4"
        >
          <v-checkbox
            v-model="ex4"
            color="orange"
            label="orange"
            value="orange"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="ex4"
            color="orange-darken-3"
            label="orange-darken-3"
            value="orange-darken-3"
            hide-details
          ></v-checkbox>
        </v-col>
      </v-row>

      <v-row class="mt-12">
        <v-col
          cols="12"
          md="4"
          sm="4"
        >
          <v-checkbox
            v-model="ex4"
            color="primary"
            label="primary"
            value="primary"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="ex4"
            color="secondary"
            label="secondary"
            value="secondary"
            hide-details
          ></v-checkbox>
        </v-col>
        <v-col
          cols="12"
          md="4"
          sm="4"
        >
          <v-checkbox
            v-model="ex4"
            color="success"
            label="success"
            value="success"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="ex4"
            color="info"
            label="info"
            value="info"
            hide-details
          ></v-checkbox>
        </v-col>
        <v-col
          cols="12"
          md="4"
          sm="4"
        >
          <v-checkbox
            v-model="ex4"
            color="warning"
            label="warning"
            value="warning"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="ex4"
            color="error"
            label="error"
            value="error"
            hide-details
          ></v-checkbox>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
  const ex4 = ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red darken-3', 'indigo darken-3', 'orange darken-3']
</script>

<script>
  export default {
    data () {
      return {
        ex4: ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red darken-3', 'indigo darken-3', 'orange darken-3'],
      }
    },
  }
</script>

```

# Vuetify component v-checkbox - slot label

Example code

```vue
<template>
  <v-container fluid>
    <v-checkbox v-model="checkbox">
      <template v-slot:label>
        <div>
          I agree that
          <v-tooltip location="bottom">
            <template v-slot:activator="{ props }">
              <a
                href="https://vuetifyjs.com"
                target="_blank"
                v-bind="props"
                @click.stop
              >
                Vuetify
              </a>
            </template>
            Opens in new window
          </v-tooltip>
          is awesome
        </div>
      </template>
    </v-checkbox>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const checkbox = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        checkbox: false,
      }
    },
  }
</script>

```
