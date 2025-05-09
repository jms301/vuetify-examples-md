# Vuetify component v-overlay - usage

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      color="error"
      @click="overlay = !overlay"
    >
      Show Overlay
    </v-btn>

    <v-overlay v-model="overlay"></v-overlay>
  </div>
</template>

<script>
  export default {
    data: () => ({
      overlay: false,
    }),

    watch: {
      overlay (val) {
        val && setTimeout(() => {
          this.overlay = false
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-overlay - prop contained

Example code

```vue
<template>
  <v-row
    align="center"
    class="ma-4"
    justify="center"
  >
    <v-card
      height="300"
      width="250"
    >
      <v-row justify="center">
        <v-btn
          class="mt-12"
          color="success"
          @click="overlay = !overlay"
        >
          Show Overlay
        </v-btn>

        <v-overlay
          v-model="overlay"
          class="align-center justify-center"
          contained
        >
          <v-btn
            color="success"
            @click="overlay = false"
          >
            Hide Overlay
          </v-btn>
        </v-overlay>
      </v-row>
    </v-card>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const overlay = ref(false)
</script>

<script>
  export default {
    data: () => ({
      overlay: false,
    }),
  }
</script>

```

# Vuetify component v-overlay - misc loader

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      append-icon="mdi-open-in-new"
      color="deep-purple-accent-4"
      @click="overlay = !overlay"
    >
      Launch Application
    </v-btn>

    <v-overlay
      :model-value="overlay"
      class="align-center justify-center"
    >
      <v-progress-circular
        color="primary"
        size="64"
        indeterminate
      ></v-progress-circular>
    </v-overlay>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const overlay = ref(false)
  watch(overlay, val => {
    val && setTimeout(() => {
      overlay.value = false
    }, 3000)
  })
</script>

<script>
  export default {
    data: () => ({
      overlay: false,
    }),

    watch: {
      overlay (val) {
        val && setTimeout(() => {
          this.overlay = false
        }, 3000)
      },
    },
  }
</script>

```

# Vuetify component v-overlay - scroll close

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-btn>
      Close

      <v-overlay
        activator="parent"
        location-strategy="connected"
        scroll-strategy="close"
      >
        <v-card class="pa-2">
          Hello!
        </v-card>
      </v-overlay>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-overlay - scroll block

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-btn>
      block

      <v-overlay
        activator="parent"
        location-strategy="connected"
        scroll-strategy="block"
      >
        <v-card class="pa-2">
          Hello!
        </v-card>
      </v-overlay>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-overlay - connected playground

Example code

```vue
<template>
  <div>
    <v-row>
      <v-col class="d-flex flex-column align-center" cols="12">
        <code>{{ code }}</code>

        <v-tooltip
          :location="location"
          :origin="origin"
          no-click-animation
        >
          <template v-slot:activator="{ props }">
            <v-btn v-bind="props" class="my-12" text="Hover Me"></v-btn>
          </template>

          <div>Overlay content</div>
        </v-tooltip>
      </v-col>

      <v-col>
        <v-radio-group v-model="locationSide" label="Location side">
          <v-radio label="top" value="top"></v-radio>
          <v-radio label="end" value="end"></v-radio>
          <v-radio label="bottom" value="bottom"></v-radio>
          <v-radio label="start" value="start"></v-radio>
        </v-radio-group>
      </v-col>

      <v-col>
        <v-radio-group v-model="locationAlign" label="Location alignment">
          <v-radio :disabled="locationSide === 'top' || locationSide === 'bottom'" label="top" value="top"></v-radio>
          <v-radio :disabled="!(locationSide === 'top' || locationSide === 'bottom')" label="start" value="start"></v-radio>
          <v-radio label="center" value="center"></v-radio>
          <v-radio :disabled="!(locationSide === 'top' || locationSide === 'bottom')" label="end" value="end"></v-radio>
          <v-radio :disabled="locationSide === 'top' || locationSide === 'bottom'" label="bottom" value="bottom"></v-radio>
        </v-radio-group>
      </v-col>

      <v-col>
        <v-radio-group v-model="originSide" label="Origin side">
          <v-radio label="auto" value="auto"></v-radio>
          <v-radio label="overlap" value="overlap"></v-radio>
          <v-radio label="top" value="top"></v-radio>
          <v-radio label="end" value="end"></v-radio>
          <v-radio label="bottom" value="bottom"></v-radio>
          <v-radio label="start" value="start"></v-radio>
        </v-radio-group>
      </v-col>

      <v-col>
        <v-radio-group v-model="originAlign" label="Origin alignment">
          <v-radio :disabled="originDisabled || originSide === 'top' || originSide === 'bottom'" label="top" value="top"></v-radio>
          <v-radio :disabled="originDisabled || !(originSide === 'top' || originSide === 'bottom')" label="start" value="start"></v-radio>
          <v-radio :disabled="originDisabled" label="center" value="center"></v-radio>
          <v-radio :disabled="originDisabled || !(originSide === 'top' || originSide === 'bottom')" label="end" value="end"></v-radio>
          <v-radio :disabled="originDisabled || originSide === 'top' || originSide === 'bottom'" label="bottom" value="bottom"></v-radio>
        </v-radio-group>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
  import { computed, ref, watch } from 'vue'

  const locationSide = ref('top')
  const locationAlign = ref('center')
  const originSide = ref('auto')
  const originAlign = ref('')

  const location = computed(() => {
    return `${locationSide.value} ${locationAlign.value}`
  })
  const origin = computed(() => {
    return originDisabled.value ? originSide.value : `${originSide.value} ${originAlign.value}`
  })
  const code = computed(() => {
    return `<v-tooltip location="${location.value}" origin="${origin.value}" />`
  })
  const originDisabled = computed(() => {
    return ['auto', 'overlap'].includes(originSide.value)
  })

  watch(locationSide, val => {
    if (['top', 'bottom'].includes(val)) {
      locationAlign.value = {
        top: 'start',
        bottom: 'end',
      }[locationAlign.value] || locationAlign.value
    } else {
      locationAlign.value = {
        start: 'top',
        end: 'bottom',
      }[locationAlign.value] || locationAlign.value
    }
  })
  watch(originDisabled, val => {
    if (!val && !originAlign.value) {
      originAlign.value = 'center'
    }
  })
</script>

```

# Vuetify component v-overlay - scroll reposition

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-btn>
      Reposition

      <v-overlay
        activator="parent"
        location-strategy="connected"
        scroll-strategy="reposition"
      >
        <v-card class="pa-2">
          Hello!
        </v-card>
      </v-overlay>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-overlay - scroll none

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-btn>
      None

      <v-overlay
        activator="parent"
        location-strategy="connected"
        scroll-strategy="none"
      >
        <v-card class="pa-2">
          Hello!
        </v-card>
      </v-overlay>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-overlay - misc advanced

Example code

```vue
<template>
  <div>
    <v-hover v-slot="{ isHovering, props }">
      <v-card
        class="mx-auto"
        max-width="344"
        v-bind="props"
      >
        <v-img src="https://cdn.vuetifyjs.com/images/cards/forest-art.jpg"></v-img>

        <v-card-text>
          <h2 class="text-h6 text-primary">
            Magento Forests
          </h2>
          Travel to the best outdoor experience on planet Earth. A vacation you will never forget!
        </v-card-text>

        <v-card-title>
          <v-rating
            :model-value="4"
            class="me-2"
            color="orange"
            density="compact"
            hover
          ></v-rating>
          <span class="text-primary text-subtitle-2">64 Reviews</span>
        </v-card-title>

        <v-overlay
          :model-value="!!isHovering"
          class="align-center justify-center"
          scrim="#036358"
          contained
        >
          <v-btn variant="flat">See more info</v-btn>
        </v-overlay>
      </v-card>
    </v-hover>
  </div>
</template>

```
