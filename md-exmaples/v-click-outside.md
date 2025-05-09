# Vuetify component v-click-outside - usage

Example code

```vue
<template>
  <v-card
    :color="active ? 'primary' : undefined"
    :dark="active"
    class="mx-auto"
    height="256"
    rounded="xl"
    width="256"
    v-click-outside="onClickOutside"
    @click="active = true"
  >
    <div class="text-h6 text-md-h4 fill-height d-flex align-center justify-center">
      {{ active ? 'Click Outside' : 'Click Me' }}
    </div>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      active: false,
    }),

    methods: {
      onClickOutside () {
        this.active = false
      },
    },
  }
</script>

```

# Vuetify component v-click-outside - option include

Example code

```vue
<template>
  <v-card
    :color="active ? 'primary' : undefined"
    :dark="active"
    class="mx-auto"
    height="256"
    rounded="xl"
    width="256"
    v-click-outside="{
      handler: onClickOutside,
      include
    }"
    @click="active = true"
  >
    <div class="text-h6 text-md-h4 fill-height d-flex align-center justify-center">
      {{ active ? 'Click Outside' : 'Click Me' }}
    </div>
  </v-card>

  <div class="d-flex justify-center">
    <v-card
      class="ma-2 included"
      rounded="lg"
    >
      <v-card-text class="text-h6">
        This element is included
      </v-card-text>
    </v-card>

    <v-card
      class="ma-2"
      rounded="lg"
    >
      <v-card-text class="text-h6">
        This element is not included
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const active = ref(false)

  function onClickOutside () {
    active.value = false
  }
  function include () {
    return [document.querySelector('.included')]
  }
</script>

<script>
  export default {
    data: () => ({
      active: false,
    }),
    methods: {
      onClickOutside () {
        this.active = false
      },
      include () {
        return [document.querySelector('.included')]
      },
    },
  }
</script>

```

# Vuetify component v-click-outside - option close on outside click

Example code

```vue
<template>
  <v-switch v-model="clickOutsideEnabled" :label="`Click outside ${clickOutsideEnabled ? 'enabled' : 'disabled'}`"></v-switch>
  <v-card
    :color="active ? 'primary' : undefined"
    :dark="active"
    class="mx-auto"
    height="256"
    rounded="xl"
    width="256"
    v-click-outside="{
      handler: onClickOutside,
      closeConditional: onCloseConditional
    }"
    @click="active = true"
  >
    <div class="text-h6 text-md-h4 fill-height d-flex align-center justify-center">
      {{ active ? 'Click Outside' : 'Click Me' }}
    </div>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const active = ref(false)
  const clickOutsideEnabled = ref(false)

  function onClickOutside () {
    active.value = false
  }
  function onCloseConditional (e) {
    return clickOutsideEnabled.value
  }
</script>

<script>
  export default {
    data: () => ({
      active: false,
      clickOutsideEnabled: false,
    }),

    methods: {
      onClickOutside () {
        this.active = false
      },
      onCloseConditional (e) {
        return this.clickOutsideEnabled
      },
    },
  }
</script>

```
