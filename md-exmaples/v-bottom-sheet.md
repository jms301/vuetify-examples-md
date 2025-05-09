# Vuetify component v-bottom-sheet - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-bottom-sheet v-bind="props">
      <template v-slot:activator="{ props: activatorProps }">
        <div class="pa-2 text-center">
          <v-btn
            v-bind="activatorProps"
            size="x-large"
            text="Click Me"
          ></v-btn>
        </div>
      </template>

      <v-card
        text="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut, eos? Nulla aspernatur odio rem, culpa voluptatibus eius debitis dolorem perspiciatis asperiores sed consectetur praesentium! Delectus et iure maxime eaque exercitationem!"
        title="Bottom Sheet"
      ></v-card>
    </v-bottom-sheet>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-bottom-sheet'
  const model = ref('default')
  const options = ['inset']

  const props = computed(() => {
    return {
      inset: model.value === 'inset' || undefined,
    }
  })

  const slots = computed(() => {
    return `
  <template v-slot:activator="{ props: activatorProps }">
    <v-btn v-bind="activatorProps" text="Click Me"></v-btn>
  </template>

  <v-card
    title="Bottom Sheet"
    text="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut, eos? Nulla aspernatur odio rem, culpa voluptatibus eius debitis dolorem perspiciatis asperiores sed consectetur praesentium! Delectus et iure maxime eaque exercitationem!"
  ></v-card>
`
  })

  const code = computed(() => {
    return `<v-bottom-sheet${propsToString(props.value)}>${slots.value}</v-bottom-sheet>`
  })
</script>

```

# Vuetify component v-bottom-sheet - misc player

Example code

```vue
<template>
  <v-bottom-sheet inset>
    <template v-slot:activator="{ props: activatorProps }">
      <div class="text-center pa-8">
        <v-btn
          v-bind="activatorProps"
          color="red"
          size="x-large"
          text="Click Me"
        ></v-btn>
      </div>
    </template>

    <v-sheet>
      <v-progress-linear model-value="50"></v-progress-linear>

      <v-list>
        <v-list-item subtitle="Fitz & The Trantrums" title="The Walker">
          <template v-slot:append>
            <div class="d-flex ga-1">
              <v-btn icon="mdi-rewind" variant="text"></v-btn>

              <v-btn icon="mdi-pause" variant="text"></v-btn>

              <v-btn icon="mdi-fast-forward" variant="text"></v-btn>
            </div>
          </template>
        </v-list-item>
      </v-list>
    </v-sheet>
  </v-bottom-sheet>
</template>

```

# Vuetify component v-bottom-sheet - misc open in list

Example code

```vue
<template>
  <v-bottom-sheet v-model="sheet">
    <template v-slot:activator="{ props: activatorProps }">
      <div class="text-center pa-8">
        <v-btn
          v-bind="activatorProps"
          color="purple"
          size="x-large"
          text="Click Me"
        ></v-btn>
      </div>
    </template>

    <v-list>
      <v-list-subheader title="Open in"></v-list-subheader>

      <v-list-item
        v-for="tile in tiles"
        :key="tile.title"
        :prepend-avatar="`https://cdn.vuetifyjs.com/images/bottom-sheets/${tile.img}`"
        :title="tile.title"
        @click="sheet = false"
      ></v-list-item>
    </v-list>
  </v-bottom-sheet>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const sheet = shallowRef(false)
  const tiles = [
    { img: 'keep.png', title: 'Keep' },
    { img: 'inbox.png', title: 'Inbox' },
    { img: 'hangouts.png', title: 'Hangouts' },
    { img: 'messenger.png', title: 'Messenger' },
    { img: 'google.png', title: 'Google+' },
  ]
</script>

<script>
  export default {
    data: () => ({
      sheet: false,
      tiles: [
        { img: 'keep.png', title: 'Keep' },
        { img: 'inbox.png', title: 'Inbox' },
        { img: 'hangouts.png', title: 'Hangouts' },
        { img: 'messenger.png', title: 'Messenger' },
        { img: 'google.png', title: 'Google+' },
      ],
    }),
  }
</script>

```

# Vuetify component v-bottom-sheet - prop model

Example code

```vue
<template>
  <div class="pa-8 text-center">
    <v-btn
      class="ma-auto"
      size="x-large"
      text="Click Me"
      @click="sheet = !sheet"
    ></v-btn>

    <v-bottom-sheet v-model="sheet">
      <v-card class="text-center" height="200">
        <v-card-text>
          <v-btn
            text="Close"
            variant="text"
            @click="sheet = !sheet"
          ></v-btn>

          <br>
          <br>

          <div>
            This is a bottom sheet using the controlled by v-model instead of activator
          </div>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const sheet = shallowRef(false)
</script>

<script>
  export default {
    data: () => ({
      sheet: false,
    }),
  }
</script>

```

# Vuetify component v-bottom-sheet - prop inset

Example code

```vue
<template>
  <div class="text-center pa-8">
    <v-btn
      class="ma-auto"
      size="x-large"
      text="Click Me"
      @click="sheet = !sheet"
    ></v-btn>

    <v-bottom-sheet v-model="sheet" inset>
      <v-card class="text-center" height="200">
        <v-card-text>
          <v-btn
            text="Close"
            variant="text"
            @click="sheet = !sheet"
          ></v-btn>

          <br>
          <br>

          <div>
            This is a bottom sheet that is using the inset prop
          </div>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const sheet = shallowRef(false)
</script>

<script>
  export default {
    data: () => ({
      sheet: false,
    }),
  }
</script>

```
