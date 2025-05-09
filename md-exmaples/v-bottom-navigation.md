# Vuetify component v-bottom-navigation - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-layout class="overflow-visible">
      <v-bottom-navigation v-bind="props">
        <v-btn value="history">
          <v-icon>mdi-history</v-icon>

          <span>Recent</span>
        </v-btn>

        <v-btn value="favorites">
          <v-icon>mdi-heart</v-icon>

          <span>Favorites</span>
        </v-btn>

        <v-btn value="nearby">
          <v-icon>mdi-map-marker</v-icon>

          <span>Nearby</span>
        </v-btn>
      </v-bottom-navigation>
    </v-layout>

    <template v-slot:configuration>
      <v-slider v-model="elevation" label="Elevation" max="24" min="0" step="1"></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-bottom-navigation'
  const model = ref('default')
  const options = ['grow', 'shift']
  const elevation = ref(4)

  const props = computed(() => {
    return {
      elevation: elevation.value === 4 ? undefined : elevation.value,
      grow: model.value === 'grow' || undefined,
      mode: model.value === 'shift' ? 'shift' : undefined,
    }
  })

  const slots = computed(() => {
    let str = ''

    str += `
  <v-btn value="recent">
    <v-icon>mdi-history</v-icon>

    <span>Recent</span>
  </v-btn>

  <v-btn value="favorites">
    <v-icon>mdi-heart</v-icon>

    <span>Favorites</span>
  </v-btn>

  <v-btn value="nearby">
    <v-icon>mdi-map-marker</v-icon>

    <span>Nearby</span>
  </v-btn>
`

    return str
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-bottom-navigation - prop shift

Example code

```vue
<template>

  <v-layout class="overflow-visible" style="height: 56px;">
    <v-bottom-navigation
      v-model="value"
      :bg-color="color"
      mode="shift"
    >
      <v-btn>
        <v-icon>mdi-television-play</v-icon>

        <span>Video</span>
      </v-btn>

      <v-btn>
        <v-icon>mdi-music-note</v-icon>

        <span>Music</span>
      </v-btn>

      <v-btn>
        <v-icon>mdi-book</v-icon>

        <span>Book</span>
      </v-btn>

      <v-btn>
        <v-icon>mdi-image</v-icon>

        <span>Image</span>
      </v-btn>
    </v-bottom-navigation>
  </v-layout>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const value = ref(1)
  const color = computed(() => {
    switch (value.value) {
      case 0: return 'blue-grey'
      case 1: return 'teal'
      case 2: return 'brown'
      case 3: return 'indigo'
      default: return 'blue-grey'
    }
  })
</script>

<script>
  export default {
    data: () => ({ value: 1 }),

    computed: {
      color () {
        switch (this.value) {
          case 0: return 'blue-grey'
          case 1: return 'teal'
          case 2: return 'brown'
          case 3: return 'indigo'
          default: return 'blue-grey'
        }
      },
    },
  }
</script>

```

# Vuetify component v-bottom-navigation - prop color

Example code

```vue
<template>
  <v-layout class="overflow-visible" style="height: 56px;">
    <v-bottom-navigation
      v-model="value"
      color="primary"
      active
    >
      <v-btn>
        <v-icon>mdi-history</v-icon>

        Recents
      </v-btn>

      <v-btn>
        <v-icon>mdi-heart</v-icon>

        Favorites
      </v-btn>

      <v-btn>
        <v-icon>mdi-map-marker</v-icon>

        <span>Nearby</span>
      </v-btn>
    </v-bottom-navigation>
  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(0)
</script>

<script>
  export default {
    data: () => ({ value: 0 }),
  }
</script>

```

# Vuetify component v-bottom-navigation - prop grow

Example code

```vue
<template>
  <v-layout class="overflow-visible" style="height: 56px;">
    <v-bottom-navigation
      v-model="value"
      color="teal"
      grow
    >
      <v-btn>
        <v-icon>mdi-history</v-icon>

        Recents
      </v-btn>

      <v-btn>
        <v-icon>mdi-heart</v-icon>

        Favorites
      </v-btn>

      <v-btn>
        <v-icon>mdi-map-marker</v-icon>

        Nearby
      </v-btn>
    </v-bottom-navigation>
  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(1)
</script>

<script>
  export default {
    data: () => ({ value: 1 }),
  }
</script>

```

# Vuetify component v-bottom-navigation - prop toggle

Example code

```vue
<template>
  <v-layout class="border rounded" style="height: 128px;">
    <div class="mx-auto my-4">
      <v-btn
        color="deep-purple"
        variant="outlined"
        @click="active = !active"
      >
        Toggle Navigation
      </v-btn>
    </div>

    <v-bottom-navigation
      :active="active"
      color="indigo"
    >
      <v-btn>
        <v-icon>mdi-history</v-icon>

        Recents
      </v-btn>

      <v-btn>
        <v-icon>mdi-heart</v-icon>

        Favorites
      </v-btn>

      <v-btn>
        <v-icon>mdi-map-marker</v-icon>

        Nearby
      </v-btn>
    </v-bottom-navigation>

  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const active = ref(true)
</script>

<script>
  export default {
    data: () => ({ active: true }),
  }
</script>

```

# Vuetify component v-bottom-navigation - prop horizontal

Example code

```vue
<template>

  <v-layout class="overflow-visible" style="height: 56px;">
    <v-bottom-navigation
      v-model="value"
      color="primary"
      horizontal
    >
      <v-btn>
        <v-icon>mdi-history</v-icon>

        Recents
      </v-btn>

      <v-btn>
        <v-icon>mdi-heart</v-icon>

        Favorites
      </v-btn>

      <v-btn>
        <v-icon>mdi-map-marker</v-icon>

        Nearby
      </v-btn>
    </v-bottom-navigation>
  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(1)
</script>

<script>
  export default {
    data: () => ({ value: 1 }),
  }
</script>

```

# Vuetify component v-bottom-navigation - prop scroll threshold

Example code

```vue
<template>
  <v-card
    class="mx-auto overflow-hidden"
    height="200"
    max-width="500"
  >
    <v-bottom-navigation
      color="white"
      scroll-target="#scroll-threshold-example"
      scroll-threshold="500"
      absolute
      hide-on-scroll
      horizontal
    >
      <v-btn>
        <span>Recents</span>

        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn>
        <span>Favorites</span>

        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn>
        <span>Nearby</span>

        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>

    <v-sheet
      id="scroll-threshold-example"
      class="overflow-y-auto pb-16"
      max-height="600"
    >
      <v-responsive height="1500"></v-responsive>
    </v-sheet>
  </v-card>
</template>

```

# Vuetify component v-bottom-navigation - prop hide on scroll

Example code

```vue
<template>
  <v-card
    class="overflow-hidden mx-auto"
    height="200"
    max-width="500"
  >
    <v-bottom-navigation
      scroll-target="#hide-on-scroll-example"
      absolute
      hide-on-scroll
      horizontal
    >
      <v-btn
        color="deep-purple-accent-4"
        variant="text"
      >
        <span>Recents</span>

        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn
        color="deep-purple-accent-4"
        variant="text"
      >
        <span>Favorites</span>

        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn
        color="deep-purple-accent-4"
        variant="text"
      >
        <span>Nearby</span>

        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>

    <v-responsive
      id="hide-on-scroll-example"
      class="overflow-y-auto"
      max-height="600"
    >
      <v-responsive height="1500"></v-responsive>
    </v-responsive>
  </v-card>
</template>

```
