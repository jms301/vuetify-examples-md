# Vuetify component v-confirm-edit - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :options="options"
    :script="script"
    name="v-avatar"
  >
    <div>
      <v-confirm-edit v-model="value" v-bind="props">
        <template v-slot:default="{ model: proxyModel, actions }">
          <v-card
            class="mx-auto"
            max-width="320"
            title="Update Field"
          >
            <template v-slot:text>
              <v-text-field
                v-model="proxyModel.value"
                messages="Modify my value"
              ></v-text-field>
            </template>

            <template v-slot:actions>
              <v-spacer></v-spacer>

              <component :is="actions"></component>
            </template>
          </v-card>
        </template>
      </v-confirm-edit>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="okText" label="Ok text"></v-text-field>
      <v-text-field v-model="cancelText" label="Cancel text"></v-text-field>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const model = ref('default')
  const options = []
  const value = ref('Egg Plant')
  const okText = ref('Ok')
  const cancelText = ref('Cancel')

  const props = computed(() => {
    return {
      'ok-text': okText.value === 'Ok' ? undefined : okText.value,
      'cancel-text': cancelText.value === 'Cancel' ? undefined : cancelText.value,
      'v-model': 'model',
    }
  })

  const slots = computed(() => {
    return `
  <template v-slot:default="{ model: proxyModel, actions }">
    <v-card
      class="mx-auto"
      max-width="320"
      title="Update Field"
    >
      <template v-slot:text>
        <v-text-field
          v-model="proxyModel.value"
          messages="Modify my value"
        ></v-text-field>
      </template>

      <template v-slot:actions>
        <v-spacer></v-spacer>

        <component :is="actions"></component>
      </template>
    </v-card>
  </template>
`
  })

  const script = computed(() => {
    return `<script setup>
  import { shallowRef } from 'vue'

  const model = shallowRef('Egg plant')
<` + '/script>'
  })

  const code = computed(() => {
    return `<v-confirm-edit${propsToString(props.value)}>${slots.value}</v-confirm-edit>`
  })
</script>

```

# Vuetify component v-confirm-edit - misc disable actions

Example code

```vue
<template>
  <div>
    <div class="d-flex justify-center">
      <v-btn-toggle
        density="comfortable"
        rounded="lg"
        border
        divided
      >
        <v-btn
          :active="Array.isArray(disabled) && disabled?.includes('cancel')"
          text="Toggle cancel"
          @click="onClick('cancel')"
        ></v-btn>

        <v-btn
          :active="Array.isArray(disabled) && disabled?.includes('save')"
          text="Toggle save"
          @click="onClick('save')"
        ></v-btn>

        <v-btn
          :active="typeof disabled === 'boolean'"
          text="Toggle Boolean"
          @click="disabled = !disabled"
        ></v-btn>

        <v-btn
          :active="disabled === undefined"
          text="Default"
          @click="disabled = undefined"
        ></v-btn>
      </v-btn-toggle>
    </div>

    <div class="d-flex justify-center align-center py-4 ga-2">
      <strong>Disabled:</strong>
      <span
        class="bg-surface-light rounded rounded-md pa-1"
        size="small"
        v-text="disabled === undefined ? 'undefined' : disabled"
      ></span>
    </div>

    <v-sheet
      class="pa-4"
      color="surface-light"
      rounded="lg"
    >
      <v-confirm-edit
        v-slot="{ model: proxyModel, actions }"
        v-model="value"
        :disabled="disabled"
      >
        <v-card class="mx-auto" max-width="400" rounded="lg" title="Update Field">
          <template v-slot:text>
            <v-text-field
              v-model="proxyModel.value"
              label="Name"
              prepend-icon="$vuetify"
              variant="outlined"
            ></v-text-field>
          </template>

          <v-divider></v-divider>

          <template v-slot:actions>
            <v-spacer></v-spacer>

            <component :is="actions"></component>
          </template>
        </v-card>
      </v-confirm-edit>
    </v-sheet>
  </div>
</template>

<script setup>
  import { ref, shallowRef } from 'vue'

  const disabled = ref([])
  const value = shallowRef('My Beach Vacation')

  function onClick (action) {
    if (!Array.isArray(disabled.value)) {
      disabled.value = []
    }

    if (disabled.value.includes(action)) {
      disabled.value = disabled.value.filter(item => item !== action)
    } else {
      disabled.value.push(action)
    }
  }
</script>

<script>
  export default {
    data () {
      return {
        disabled: [],
        value: 'My Beach Vacation',
      }
    },

    methods: {
      onClick (action) {
        if (!Array.isArray(this.disabled)) {
          this.disabled = []
        }

        if (this.disabled.includes(action)) {
          this.disabled = this.disabled.filter(item => item !== action)
        } else {
          this.disabled.push(action)
        }
      },
    },
  }
</script>

```

# Vuetify component v-confirm-edit - misc date picker

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="328"
    rounded="lg"
    border
  >
    <v-confirm-edit v-model="date">
      <template v-slot:default="{ model: proxyModel, actions }">
        <v-date-picker v-model="proxyModel.value">
          <template v-slot:actions>
            <component :is="actions"></component>
          </template>
        </v-date-picker>
      </template>
    </v-confirm-edit>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const date = shallowRef()
</script>

```
