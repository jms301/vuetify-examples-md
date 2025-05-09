# Vuetify component v-app-bar - usage

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
      <v-app-bar v-bind="props">
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Application Bar</v-app-bar-title>

        <template v-if="actions" v-slot:append>
          <v-btn icon="mdi-heart"></v-btn>

          <v-btn icon="mdi-magnify"></v-btn>

          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
      </v-app-bar>

      <v-main style="height: 75px;"></v-main>
    </v-layout>

    <template v-slot:configuration>
      <v-checkbox v-model="actions" label="Actions"></v-checkbox>

      <v-slider v-model="elevation" label="Elevation" max="24" min="0" step="1"></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-app-bar'
  const model = ref('default')
  const actions = ref(false)
  const elevation = ref(2)
  const options = ['collapse', 'rounded']

  const props = computed(() => {
    return {
      collapse: model.value === 'collapse' ? true : undefined,
      elevation: elevation.value === 4 ? undefined : elevation.value,
      rounded: model.value === 'rounded' ? true : undefined,
    }
  })

  const slots = computed(() => {
    let str = ''

    str += `
  <template v-slot:prepend>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
  </template>

  <v-app-bar-title>Application Bar</v-app-bar-title>
`

    if (actions.value) {
      str += `
  <template v-slot:append>
    <v-btn icon="mdi-heart"></v-btn>

    <v-btn icon="mdi-magnify"></v-btn>

    <v-btn icon="mdi-dots-vertical"></v-btn>
  </template>
`
    }

    return str
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-app-bar - prop dense

Example code

```vue
<template>
  <div>
    <v-app-bar
      color="deep-purple-accent-4"
      dense
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Page title</v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            v-bind="props"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>

```

# Vuetify component v-app-bar - misc menu

Example code

```vue
<template>
  <v-layout>
    <v-app-bar
      color="#6A76AB"
      scroll-behavior="shrink fade-image"
      scroll-target="#scrolling-techniques-4"
      src="https://picsum.photos/1920/1080?random"
      absolute
    >
      <template v-slot:image>
        <v-img gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn
            color="yellow"
            icon
            v-bind="props"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item>
            <v-list-item-title>Click Me 1</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Click Me 2</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Click Me 3</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Click Me 4</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <template v-slot:extension>
        <v-tabs align-tabs="title">
          <v-tab>Tab 1</v-tab>

          <v-tab>Tab 2</v-tab>

          <v-tab>Tab 3</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-4"
      class="overflow-y-auto"
      max-height="600"
      width="100%"
    >
      <v-container style="height: 1000px;"></v-container>
    </v-sheet>
  </v-layout>
</template>

```

# Vuetify component v-app-bar - prop density

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="448"
  >
    <v-layout>
      <v-app-bar
        color="primary"
        density="compact"
      >
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Photos</v-app-bar-title>

        <template v-slot:append>
          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
      </v-app-bar>

      <v-main>
        <v-container fluid>
          <v-row dense>
            <v-col
              v-for="n in 8"
              :key="n"
              cols="3"
            >
              <v-sheet
                color="surface-variant-alt"
                height="96"
              ></v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

```

# Vuetify component v-app-bar - prop image

Example code

```vue
<template>
  <v-card class="mx-auto" color="grey-lighten-3" max-width="448">
    <v-layout>
      <v-app-bar
        color="teal-darken-4"
        image="https://picsum.photos/1920/1080?random"
      >
        <template v-slot:image>
          <v-img
            gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
          ></v-img>
        </template>

        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Title</v-app-bar-title>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-app-bar>

      <v-main>
        <v-container fluid>
          <v-row dense>
            <v-col
              v-for="n in 4"
              :key="n"
              cols="12"
            >
              <v-card
                :subtitle="`Subtitle for Content ${n}`"
                :title="`Content ${n}`"
                text="Lorem ipsum dolor sit amet consectetur, adipisicing elit.?"
              ></v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

```

# Vuetify component v-app-bar - prop prominent

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="448">
    <v-layout>
      <v-app-bar
        color="info"
        density="prominent"
      >
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>My Recent Trips</v-app-bar-title>

        <template v-slot:append>
          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
      </v-app-bar>

      <v-main>
        <v-container fluid>
          <v-card
            class="mb-2"
            density="compact"
            prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg"
            subtitle="Salsa, merengue, y cumbia"
            title="Cuba"
            variant="text"
            border
          >
            <v-img height="128" src="https://picsum.photos/512/128?image=660" cover></v-img>

            <v-card-text>
              During my last trip to South America, I spent 2 weeks traveling through Patagonia in Chile.
            </v-card-text>

            <template v-slot:actions>
              <v-btn color="primary" variant="text">View More</v-btn>

              <v-btn color="primary" variant="text">See in Map</v-btn>
            </template>
          </v-card>

          <v-card
            density="comfortable"
            prepend-avatar="https://randomuser.me/api/portraits/women/17.jpg"
            subtitle="Salsa, merengue, y cumbia"
            title="Florida"
            variant="text"
            border
          >
            <v-img height="128" src="https://picsum.photos/512/128?random" cover></v-img>

            <v-card-text>
              During my last trip to Florida, I spent 2 weeks traveling through the Everglades.
            </v-card-text>

            <template v-slot:actions>
              <v-btn color="primary" variant="text">View More</v-btn>

              <v-btn color="primary" variant="text">See in Map</v-btn>
            </template>
          </v-card>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

```

# Vuetify component v-app-bar - misc app bar nav

Example code

```vue
<template>
  <v-layout style="overflow: hidden">
    <v-app-bar
      color="deep-purple"
      absolute
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        v-model="group"
        color="deep-purple-accent-4"
        density="compact"
        nav
      >
        <v-list-item prepend-icon="mdi-home" title="Home" value="home"></v-list-item>

        <v-list-item prepend-icon="mdi-account" title="Account" value="account"></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-card
        class="mx-auto overflow-hidden"
        height="400"
      ></v-card>
    </v-main>
  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const drawer = ref(false)
  const group = ref(null)
</script>

<script>
  export default {
    data: () => ({
      drawer: false,
      group: null,
    }),
  }
</script>

```

# Vuetify component v-app-bar - prop scroll behavior

Example code

```vue
<template>
  <AppSheet class="mb-6">
    <ExamplesUsageExample
      v-model="model"
      :code="code"
      :name="name"
      :options="options"
    >
      <v-layout class="overflow-visible" style="height: 300px">
        <v-main id="scroll-behavior-layout" class="pt-0" scrollable>
          <v-app-bar
            v-bind="props"
            color="secondary"
            scroll-target="#scroll-behavior-layout > .v-main__scroller"
            style="position: sticky"
          >
            <template v-slot:prepend>
              <v-app-bar-nav-icon></v-app-bar-nav-icon>
            </template>

            <v-app-bar-title>Application Bar</v-app-bar-title>

            <template v-if="actions" v-slot:append>
              <v-btn icon="mdi-heart"></v-btn>

              <v-btn icon="mdi-magnify"></v-btn>

              <v-btn icon="mdi-dots-vertical"></v-btn>
            </template>
          </v-app-bar>

          <div style="height: 1000px"></div>
        </v-main>
      </v-layout>

      <template v-slot:configuration>
        <v-checkbox v-for="option in behaviors" :key="option.value" v-model="selectedBehaviors" :label="option.title" :value="option.value"></v-checkbox>
        <v-divider></v-divider>
        <v-checkbox v-model="selectedBehaviors" label="Inverted" value="inverted"></v-checkbox>
        <v-slider v-model="scrollThreshold" label="Threshold" max="1000" min="0" step="1"></v-slider>
      </template>
    </ExamplesUsageExample>
  </AppSheet>
</template>

<script setup>
  const name = 'v-app-bar'
  const model = ref('default')
  const options = []

  const actions = ref(false)
  const scrollThreshold = ref(300)
  const selectedBehaviors = ref([])
  const behaviors = [
    { value: 'hide', title: 'Hide' },
    { value: 'collapse', title: 'Collapse' },
    { value: 'elevate', title: 'Elevate' },
    { value: 'fade-image', title: 'Fade image' },
  ]

  const props = computed(() => {
    return {
      'scroll-behavior': selectedBehaviors.value.join(' ') || undefined,
      'scroll-threshold': scrollThreshold.value === 300 ? undefined : String(scrollThreshold.value),
      image: selectedBehaviors.value.includes('fade-image') ? 'https://picsum.photos/1920/1080?random' : undefined,
    }
  })

  const slots = computed(() => {
    let str = ''

    if (actions.value) {
      str += `
  <template v-slot:append>
    <v-btn icon="mdi-heart"></v-btn>

    <v-btn icon="mdi-magnify"></v-btn>

    <v-btn icon="mdi-dots-vertical"></v-btn>
  </template>
`
    }

    return str
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```
