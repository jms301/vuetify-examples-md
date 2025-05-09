# Vuetify component v-toolbar - usage

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
      <v-toolbar v-bind="props">
        <template v-slot:append>
          <v-btn icon="mdi-menu"></v-btn>

          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
      </v-toolbar>
    </div>

    <template v-slot:configuration>
      <v-select v-model="density" :items="['default', 'comfortable', 'compact']" label="Density"></v-select>

      <v-text-field v-model="title" label="Title" clearable></v-text-field>

      <v-checkbox v-model="collapse" label="Collapsed"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-toolbar'
  const model = ref('default')
  const collapse = ref()
  const density = ref('default')
  const title = ref('Toolbar')
  const options = ['elevated', 'bordered']
  const props = computed(() => {
    return {
      border: model.value === 'bordered' ? true : undefined,
      collapse: collapse.value || undefined,
      density: density.value === 'default' ? undefined : density.value,
      elevation: model.value === 'elevated' ? 8 : undefined,
      title: title.value || undefined,
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

# Vuetify component v-toolbar - prop dense

Example code

```vue
<template>
  <v-card height="200">
    <v-toolbar density="compact" title="Toolbar"></v-toolbar>
  </v-card>
</template>

```

# Vuetify component v-toolbar - prop extended

Example code

```vue
<template>
  <v-card height="200">
    <v-toolbar extended>
      <v-toolbar-title text="Toolbar"></v-toolbar-title>

      <template v-slot:append>
        <v-btn icon="mdi-magnify"></v-btn>

        <v-btn icon="mdi-heart"></v-btn>

        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-toolbar>
  </v-card>
</template>

```

# Vuetify component v-toolbar - prop background

Example code

```vue
<template>
  <v-card height="200">
    <v-toolbar class="text-white" image="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
      <v-btn icon="mdi-menu"></v-btn>

      <v-toolbar-title text="Toolbar"></v-toolbar-title>

      <v-btn icon="mdi-export"></v-btn>
    </v-toolbar>
  </v-card>
</template>

```

# Vuetify component v-toolbar - prop collapse

Example code

```vue
<template>
  <v-card>
    <v-toolbar :collapse="collapse" title="Toolbar">
      <template v-slot:append>
        <div class="d-flex ga-1">
          <v-btn icon="mdi-magnify"></v-btn>

          <v-btn icon="mdi-dots-vertical"></v-btn>
        </div>
      </template>
    </v-toolbar>

    <v-card-text class="text-center pa-8">
      <v-btn
        color="surface-variant"
        text="Toggle"
        @click="collapse = !collapse"
      ></v-btn>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const collapse = shallowRef(true)
</script>

```

# Vuetify component v-toolbar - misc flexible and card

Example code

```vue
<template>
  <v-card rounded="lg" border flat>
    <v-toolbar
      color="primary"
      extended
      flat
    >
      <template v-slot:prepend>
        <v-btn icon="mdi-menu"></v-btn>
      </template>
    </v-toolbar>

    <v-card
      class="mx-auto mt-n16 mb-4"
      elevation="4"
      height="200"
      max-width="600"
    >
      <v-toolbar>
        <v-toolbar-title text="Title"></v-toolbar-title>

        <template v-slot:append>
          <div class="d-flex ga-1">
            <v-btn icon="mdi-magnify">
            </v-btn>

            <v-btn icon="mdi-apps">
            </v-btn>

            <v-btn icon="mdi-dots-vertical">
            </v-btn>
          </div>
        </template>
      </v-toolbar>

      <v-divider></v-divider>
    </v-card>

    <v-footer class="justify-center text-caption" color="surface-variant">
      {{ new Date().getFullYear() }} — <strong>Vuetify, LLC</strong>
    </v-footer>
  </v-card>
</template>

```

# Vuetify component v-toolbar - prop extension height

Example code

```vue
<template>
  <v-card height="200">
    <v-toolbar extension-height="100" title="Toolbar" extended>

      <template v-slot:append>
        <v-btn icon="mdi-magnify"></v-btn>
        <v-btn icon="mdi-heart"></v-btn>
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-toolbar>
  </v-card>
</template>

```

# Vuetify component v-toolbar - misc contextual action bar

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="500">
    <v-toolbar :color="selection.length ? 'surface-variant' : 'deep-purple accent-4'">
      <template v-slot:prepend>
        <v-fade-transition hide-on-leave>
          <v-btn
            :key="selection.length > 0"
            :icon="selection.length ? 'mdi-close' : 'mdi-menu'"
            @click="onClick"
          ></v-btn>
        </v-fade-transition>
      </template>

      <v-toolbar-title :text="selection.length ? `${selection.length} selected` : 'Photos'"></v-toolbar-title>

      <template v-slot:append>
        <v-fade-transition hide-on-leave>
          <v-btn
            v-if="selection.length"
            key="export"
            icon="mdi-export-variant"
          ></v-btn>
        </v-fade-transition>

        <v-fade-transition hide-on-leave>
          <v-btn
            v-if="selection.length"
            key="delete"
            icon="mdi-delete"
          ></v-btn>
        </v-fade-transition>

        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-toolbar>

    <v-card-text>
      <v-select
        v-model="selection"
        :items="items"
        hint="Make a selection"
        label="Select an option"
        clearable
        multiple
        open-on-clear
        persistent-hint
      ></v-select>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const items = ['Foo', 'Bar', 'Fizz', 'Buzz']

  const selection = shallowRef([])

  function onClick () {
    if (!selection.value.length) return

    selection.value = []
  }
</script>

<script>
  export default {
    data: () => ({
      selection: [],
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }),

    methods: {
      onClick () {
        if (!this.selection.length) return

        this.selection = []
      },
    },
  }
</script>

```

# Vuetify component v-toolbar - prop floating with search

Example code

```vue
<template>
  <v-card
    height="300"
    image="https://cdn.vuetifyjs.com/images/toolbar/map.jpg"
    border
    flat
  >
    <template v-slot:text>
      <v-toolbar rounded="lg" border floating>
        <div class="px-4">
          <v-text-field
            density="compact"
            placeholder="Search"
            prepend-inner-icon="mdi-magnify"
            variant="solo"
            width="200"
            flat
            hide-details
            single-line
          ></v-text-field>
        </div>

        <template v-slot:append>
          <v-btn
            color="medium-emphasis"
            density="comfortable"
            icon="mdi-crosshairs-gps"
          ></v-btn>

          <v-btn
            class="ms-1"
            color="medium-emphasis"
            density="comfortable"
            icon="mdi-dots-vertical"
          ></v-btn>
        </template>
      </v-toolbar>
    </template>
  </v-card>
</template>

```

# Vuetify component v-toolbar - slot extension

Example code

```vue
<template>
  <v-card height="200">
    <v-toolbar extended>
      <v-toolbar-title text="Toolbar"></v-toolbar-title>

      <template v-slot:extension>
        <v-tabs>
          <v-tab text="Tab 1"></v-tab>
          <v-tab text="Tab 2"></v-tab>
          <v-tab text="Tab 3"></v-tab>
        </v-tabs>
      </template>
    </v-toolbar>
  </v-card>
</template>

```
