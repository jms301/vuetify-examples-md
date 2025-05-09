# Vuetify component v-empty-state - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-empty-state
      v-bind="props"
    ></v-empty-state>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-empty-state'
  const model = ref('default')
  const options = []

  const props = computed(() => {
    return {
      headline: 'Whoops, 404',
      title: 'Page not found',
      text: 'The page you were looking for does not exist',
      image: 'https://vuetifyjs.b-cdn.net/docs/images/logos/v.png',
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-empty-state - misc astro cat

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="360"
    variant="flat"
    border
  >
    <v-layout>
      <v-system-bar class="ga-1" color="surface-light">
        <v-icon icon="mdi-square" size="x-small"></v-icon>

        <v-icon icon="mdi-circle" size="x-small"></v-icon>

        <v-icon icon="mdi-triangle" size="x-small"></v-icon>
      </v-system-bar>

      <v-app-bar title="My Library">
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <template v-slot:extension>
          <v-tabs v-model="tabs" color="#4c00d5" grow>
            <v-tab text="My Movies"></v-tab>

            <v-tab text="My Tv Shows"></v-tab>
          </v-tabs>
        </template>
      </v-app-bar>

      <v-main>
        <div class="pt-4 pb-16">
          <v-window v-model="tabs">
            <v-window-item class="pa-2" value="0">
              <v-card>
                <v-empty-state
                  class="pa-0"
                  image="https://vuetifyjs.b-cdn.net/docs/images/components/v-empty-state/astro-cat.svg"
                  size="200"
                >
                  <template v-slot:media>
                    <v-sheet class="py-4 mb-4" color="#fdefff">
                      <v-img></v-img>
                    </v-sheet>
                  </template>

                  <template v-slot:title>
                    <div class="text-h6 text-high-emphasis">Get Started</div>
                  </template>

                  <template v-slot:text>
                    <div class="text-body-2 font-weight-medium text-medium-emphasis">
                      Find a great movie, then relax and enjoy with the Movies & TV app.
                    </div>
                  </template>

                  <template v-slot:actions>
                    <v-spacer></v-spacer>

                    <v-btn color="#4c00d5" text="Shop Movies"></v-btn>

                    <v-spacer></v-spacer>
                  </template>
                </v-empty-state>
              </v-card>
            </v-window-item>

            <v-window-item class="pa-2" value="0">
              <v-card>
                <v-empty-state
                  class="pa-0"
                  image="https://vuetifyjs.b-cdn.net/docs/images/components/v-empty-state/astro-dog.svg"
                  size="200"
                >
                  <template v-slot:media>
                    <v-sheet class="py-4 mb-4" color="#fdefff">
                      <v-img></v-img>
                    </v-sheet>
                  </template>

                  <template v-slot:title>
                    <div class="text-h6 text-high-emphasis">Get Started</div>
                  </template>

                  <template v-slot:text>
                    <div class="text-body-2 font-weight-medium text-medium-emphasis">
                      Watch your favorite TV Shows with the Movies & TV app.
                    </div>
                  </template>

                  <template v-slot:actions>
                    <v-spacer></v-spacer>

                    <v-btn color="#4c00d5" text="Shop TV Shows"></v-btn>

                    <v-spacer></v-spacer>
                  </template>
                </v-empty-state>
              </v-card>
            </v-window-item>
          </v-window>
        </div>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const tabs = shallowRef(0)
</script>

<script>
  export default {
    data: () => ({
      tabs: 0,
    }),
  }
</script>

```

# Vuetify component v-empty-state - slot title

Example code

```vue
<template>
  <v-empty-state icon="$success">
    <template v-slot:media>
      <v-icon color="surface-variant"></v-icon>
    </template>

    <template v-slot:headline>
      <div class="text-h4">
        All Done For Now!
      </div>
    </template>

    <template v-slot:title>
      <div class="text-h6">
        You're all caught up.
      </div>
    </template>

    <template v-slot:text>
      <div class="text-medium-emphasis text-caption">
        Great job on completing all your tasks! This might be a good time to relax or consider planning your next set of goals. If you think of something new, just hit the button below to add a new task.
      </div>
    </template>
  </v-empty-state>
</template>

```

# Vuetify component v-empty-state - misc astro dog

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="360">
    <v-layout>
      <v-system-bar class="ga-1" color="#4c00d5">
        <v-icon icon="mdi-square" size="x-small"></v-icon>

        <v-icon icon="mdi-circle" size="x-small"></v-icon>

        <v-icon icon="mdi-triangle" size="x-small"></v-icon>
      </v-system-bar>

      <v-app-bar color="#6200ee" title="Drafts">
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <template v-slot:append>
          <v-btn icon="mdi-magnify"></v-btn>

          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
      </v-app-bar>

      <v-main>
        <v-empty-state
          image="https://vuetifyjs.b-cdn.net/docs/images/components/v-empty-state/astro-dog.svg"
          size="200"
          text-width="250"
        >
          <template v-slot:media>
            <v-img class="mb-8"></v-img>
          </template>

          <template v-slot:title>
            <div class="text-h6 text-high-emphasis">Empty in drafts</div>
          </template>

          <template v-slot:text>
            <div class="text-body-1">Save a draft message and it will show up here</div>
          </template>
        </v-empty-state>
      </v-main>

      <v-layout-item
        class="text-end"
        position="bottom"
        size="80"
        model-value
      >
        <v-btn
          class="ma-4"
          color="#4c00d5"
          elevation="8"
          icon="mdi-plus"
        ></v-btn>
      </v-layout-item>
    </v-layout>
  </v-card>
</template>

```

# Vuetify component v-empty-state - prop actions

Example code

```vue
<template>
  <v-empty-state
    action-text="Retry Request"
    image="https://cdn.vuetifyjs.com/docs/images/components/v-empty-state/connection.svg"
    text="There might be a problem with your connection or our servers. Please check your internet connection or try again later. We appreciate your patience."
    title="Something Went Wrong"
    @click:action="onClickAction"
  ></v-empty-state>
</template>

<script setup>
  function onClickAction () {
    alert('You clicked the action button')
  }
</script>

<script>
  export default {
    methods: {
      onClickAction () {
        alert('You clicked the action button')
      },
    },
  }
</script>

```

# Vuetify component v-empty-state - slot default

Example code

```vue
<template>
  <v-empty-state
    headline="Welcome,"
    icon="$vuetify"
    title="What would you like to do today?"
  >
    <v-container>
      <v-row>
        <v-col cols="12" md="6">
          <v-card
            href="https://vuetifyjs.com/introduction/why-vuetify/#feature-guides"
            prepend-icon="$vuetify"
            target="_blank"
            text="Start with our dedicated feature guides"
            title="Learn Vuetify"
          ></v-card>
        </v-col>

        <v-col cols="12" md="6">
          <v-card
            href="https://play.vuetifyjs.com"
            prepend-icon="$vuetify-play"
            target="_blank"
            text="Test Vuetify out in our playground"
            title="Create a Playground"
          ></v-card>
        </v-col>

        <v-col cols="12" md="6">
          <v-card
            href="https://bin.vuetifyjs.com"
            prepend-icon="mdi-delete"
            target="_blank"
            text="Create a new bin to store your code"
            title="Create a Bin"
          ></v-card>
        </v-col>

        <v-col cols="12" md="6">
          <v-card
            href="https://issues.vuetifyjs.com"
            prepend-icon="$warning"
            target="_blank"
            text="File a bug report for Vuetify"
            title="Report a Bug"
          ></v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-empty-state>
</template>

```

# Vuetify component v-empty-state - prop content

Example code

```vue
<template>
  <v-empty-state
    headline="No Messages Yet"
    text="You haven't received any messages yet. When you do, they'll appear here."
    title="Check back later."
    @click:action="onClickAction"
  ></v-empty-state>
</template>

<script setup>
  function onClickAction () {
    alert('You clicked the action button')
  }
</script>

```

# Vuetify component v-empty-state - prop media

Example code

```vue
<template>
  <v-empty-state
    icon="mdi-magnify"
    text="Try adjusting your search terms or filters. Sometimes less specific terms or broader queries can help you find what you're looking for."
    title="We couldn't find a match."
  ></v-empty-state>
</template>

```

# Vuetify component v-empty-state - slot actions

Example code

```vue
<template>
  <v-empty-state image="https://cdn.vuetifyjs.com/docs/images/components/v-empty-state/teamwork.png">
    <template v-slot:title>
      <div class="text-subtitle-2 mt-8">
        Manage your inventory transfers
      </div>
    </template>

    <template v-slot:text>
      <div class="text-caption">
        Track and receive your incoming inventory from suppliers
      </div>
    </template>

    <template v-slot:actions>
      <v-btn
        class="text-none"
        color="white"
        elevation="1"
        rounded="lg"
        size="small"
        text="Learn more"
        width="96"
      ></v-btn>

      <v-btn
        class="text-none"
        elevation="1"
        rounded="lg"
        size="small"
        text="Add transfer"
        width="96"
      ></v-btn>
    </template>
  </v-empty-state>
</template>

```
