# Vuetify component v-tabs - usage

Example code

```vue
<template>
  <v-card>
    <v-tabs
      v-model="tab"
      bg-color="primary"
    >
      <v-tab value="one">Item One</v-tab>
      <v-tab value="two">Item Two</v-tab>
      <v-tab value="three">Item Three</v-tab>
    </v-tabs>

    <v-card-text>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="one">
          One
        </v-tabs-window-item>

        <v-tabs-window-item value="two">
          Two
        </v-tabs-window-item>

        <v-tabs-window-item value="three">
          Three
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      tab: null,
    }),
  }
</script>

```

# Vuetify component v-tabs - prop stacked

Example code

```vue
<template>
  <v-card>
    <v-tabs
      v-model="tab"
      align-tabs="center"
      bg-color="deep-purple-accent-4"
      stacked
    >
      <v-tab value="tab-1">
        <v-icon icon="mdi-phone"></v-icon>

        Recents
      </v-tab>

      <v-tab value="tab-2">
        <v-icon icon="mdi-heart"></v-icon>

        Favorites
      </v-tab>

      <v-tab value="tab-3">
        <v-icon icon="mdi-account-box"></v-icon>

        Nearby
      </v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="i in 3"
        :key="i"
        :value="'tab-' + i"
      >
        <v-card>
          <v-card-text>{{ text }}</v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tab = ref(null)

  const text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
</script>

<script>
  export default {
    data () {
      return {
        tab: null,
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>

```

# Vuetify component v-tabs - misc dynamic

Example code

```vue
<template>
  <v-card>
    <v-tabs
      v-model="tab"
      bg-color="red-lighten-2"
    >
      <v-tab
        v-for="n in length"
        :key="n"
        :text="`Item ${n}`"
        :value="n"
      ></v-tab>
    </v-tabs>

    <v-card-text class="text-center">
      <v-btn
        :disabled="!length"
        text="Remove Tab"
        variant="text"
        @click="length--"
      ></v-btn>

      <v-divider
        class="mx-4"
        vertical
      ></v-divider>

      <v-btn
        text="Add Tab"
        variant="text"
        @click="length++"
      ></v-btn>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const length = ref(15)
  const tab = ref(null)

  watch(length, val => {
    tab.value = val - 1
  })
</script>

<script>
  export default {
    data: () => ({
      length: 15,
      tab: null,
    }),

    watch: {
      length (val) {
        this.tab = val - 1
      },
    },
  }
</script>

```

# Vuetify component v-tabs - prop align tabs title

Example code

```vue
<template>
  <v-card>
    <v-toolbar color="primary">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Your Dashboard</v-toolbar-title>

      <v-btn icon="mdi-magnify"></v-btn>

      <v-btn icon="mdi-dots-vertical"></v-btn>

      <template v-slot:extension>
        <v-tabs
          v-model="tab"
          align-tabs="title"
        >
          <v-tab
            v-for="item in items"
            :key="item"
            :text="item"
            :value="item"
          ></v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="item in items"
        :key="item"
        :value="item"
      >
        <v-card flat>
          <v-card-text v-text="text"></v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tab = ref(null)

  const items = [
    'web',
    'shopping',
    'videos',
    'images',
    'news',
  ]
  const text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
</script>

<script>
  export default {
    data () {
      return {
        tab: null,
        items: [
          'web', 'shopping', 'videos', 'images', 'news',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>

```

# Vuetify component v-tabs - misc content

Example code

```vue
<template>
  <v-card>
    <v-toolbar color="primary">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Page title</v-toolbar-title>

      <v-btn icon="mdi-magnify"></v-btn>

      <v-btn icon="mdi-dots-vertical"></v-btn>

      <template v-slot:extension>
        <v-tabs
          v-model="model"
          align-tabs="center"
        >
          <v-tab
            v-for="i in 3"
            :key="i"
            :text="`Item ${i}`"
            :value="i"
          ></v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-window v-model="model">
      <v-tabs-window-item
        v-for="i in 3"
        :key="i"
        :value="i"
      >
        <v-card>
          <v-card-text>{{ text }}</v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

  const model = ref('tab-2')
</script>

<script>
  export default {
    data () {
      return {
        model: 'tab-2',
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>

```

# Vuetify component v-tabs - misc dynamic height

Example code

```vue
<template>
  <v-card>
    <v-toolbar color="purple" flat>
      <v-text-field
        append-icon="mdi-microphone"
        class="mx-4"
        label="Search"
        prepend-inner-icon="mdi-magnify"
        variant="solo-inverted"
        flat
        hide-details
      ></v-text-field>

      <template v-slot:extension>
        <v-tabs
          v-model="tabs"
          align-tabs="center"
        >
          <v-tab
            v-for="n in 3"
            :key="n"
            :text="`Item ${n}`"
          ></v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-window v-model="tabs">
      <v-tabs-window-item>
        <v-card flat>
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          </v-card-text>
        </v-card>
      </v-tabs-window-item>
      <v-tabs-window-item>
        <v-card flat>
          <v-card-title class="text-h5">
            An awesome title
          </v-card-title>
          <v-card-text>
            <p>
              Duis lobortis massa imperdiet quam. Donec vitae orci sed dolor rutrum auctor. Vestibulum facilisis, purus nec pulvinar iaculis, ligula mi congue nunc, vitae euismod ligula urna in dolor. Praesent congue erat at massa.
            </p>

            <p>
              Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Pellentesque egestas, neque sit amet convallis pulvinar, justo nulla eleifend augue, ac auctor orci leo non est. Etiam sit amet orci eget eros faucibus tincidunt. Donec sodales sagittis magna.
            </p>

            <p class="mb-0">
              Ut leo. Suspendisse potenti. Duis vel nibh at velit scelerisque suscipit. Fusce pharetra convallis urna.
            </p>
          </v-card-text>
        </v-card>
      </v-tabs-window-item>
      <v-tabs-window-item>
        <v-card flat>
          <v-card-title class="text-h5">
            An even better title
          </v-card-title>
          <v-card-text>
            <p>
              Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Sed hendrerit. Maecenas malesuada. Vestibulum ullamcorper mauris at ligula. Proin faucibus arcu quis ante.
            </p>

            <p class="mb-0">
              Etiam vitae tortor. Curabitur ullamcorper ultricies nisi. Sed magna purus, fermentum eu, tincidunt eu, varius ut, felis. Aliquam lobortis. Suspendisse potenti.
            </p>
          </v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tabs = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        tabs: null,
      }
    },
  }
</script>

```

# Vuetify component v-tabs - prop center active

Example code

```vue
<template>
  <v-card>
    <v-tabs
      bg-color="deep-purple-darken-4"
      center-active
    >
      <v-tab>One</v-tab>
      <v-tab>Two</v-tab>
      <v-tab>Three</v-tab>
      <v-tab>Four</v-tab>
      <v-tab>Five</v-tab>
      <v-tab>Six</v-tab>
      <v-tab>Seven</v-tab>
      <v-tab>Eight</v-tab>
      <v-tab>Nine</v-tab>
      <v-tab>Ten</v-tab>
      <v-tab>Eleven</v-tab>
      <v-tab>Twelve</v-tab>
      <v-tab>Thirteen</v-tab>
      <v-tab>Fourteen</v-tab>
      <v-tab>Fifteen</v-tab>
      <v-tab>Sixteen</v-tab>
      <v-tab>Seventeen</v-tab>
      <v-tab>Eighteen</v-tab>
      <v-tab>Nineteen</v-tab>
      <v-tab>Twenty</v-tab>
    </v-tabs>
  </v-card>
</template>

```

# Vuetify component v-tabs - prop direction

Example code

```vue
<template>
  <v-card>
    <v-toolbar color="primary" title="User Profile">
    </v-toolbar>

    <div class="d-flex flex-row">
      <v-tabs
        v-model="tab"
        color="primary"
        direction="vertical"
      >
        <v-tab prepend-icon="mdi-account" text="Option 1" value="option-1"></v-tab>
        <v-tab prepend-icon="mdi-lock" text="Option 2" value="option-2"></v-tab>
        <v-tab prepend-icon="mdi-access-point" text="Option 3" value="option-3"></v-tab>
      </v-tabs>

      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="option-1">
          <v-card flat>
            <v-card-text>
              <p>
                Sed aliquam ultrices mauris. Donec posuere vulputate arcu. Morbi ac felis. Etiam feugiat lorem non metus. Sed a libero.
              </p>

              <p>
                Nam ipsum risus, rutrum vitae, vestibulum eu, molestie vel, lacus. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Aliquam lobortis. Aliquam lobortis. Suspendisse non nisl sit amet velit hendrerit rutrum.
              </p>

              <p class="mb-0">
                Phasellus dolor. Fusce neque. Fusce fermentum odio nec arcu. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Phasellus blandit leo ut odio.
              </p>
            </v-card-text>
          </v-card>
        </v-tabs-window-item>

        <v-tabs-window-item value="option-2">
          <v-card flat>
            <v-card-text>
              <p>
                Morbi nec metus. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Nunc sed turpis.
              </p>

              <p>
                Suspendisse feugiat. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In hac habitasse platea dictumst. Fusce ac felis sit amet ligula pharetra condimentum.
              </p>

              <p>
                Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Nam commodo suscipit quam. In consectetuer turpis ut velit. Sed cursus turpis vitae tortor. Aliquam eu nunc.
              </p>

              <p>
                Etiam ut purus mattis mauris sodales aliquam. Ut varius tincidunt libero. Aenean viverra rhoncus pede. Duis leo. Fusce fermentum odio nec arcu.
              </p>

              <p class="mb-0">
                Donec venenatis vulputate lorem. Aenean viverra rhoncus pede. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Fusce commodo aliquam arcu. Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi.
              </p>
            </v-card-text>
          </v-card>
        </v-tabs-window-item>

        <v-tabs-window-item value="option-3">
          <v-card flat>
            <v-card-text>
              <p>
                Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
              </p>

              <p class="mb-0">
                Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
              </p>
            </v-card-text>
          </v-card>
        </v-tabs-window-item>
      </v-tabs-window>
    </div>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tab = ref('option-1')
</script>

<script>
  export default {
    data: () => ({
      tab: 'option-1',
    }),
  }
</script>

```

# Vuetify component v-tabs - prop align tabs end

Example code

```vue
<template>
  <v-card>
    <v-tabs
      v-model="tab"
      align-tabs="end"
      color="deep-purple-accent-4"
    >
      <v-tab :value="1">Landscape</v-tab>
      <v-tab :value="2">City</v-tab>
      <v-tab :value="3">Abstract</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="n in 3"
        :key="n"
        :value="n"
      >
        <v-container fluid>
          <v-row>
            <v-col
              v-for="i in 6"
              :key="i"
              cols="12"
              md="4"
            >
              <v-img
                :lazy-src="`https://picsum.photos/10/6?image=${i * n * 5 + 10}`"
                :src="`https://picsum.photos/500/300?image=${i * n * 5 + 10}`"
                height="205"
                cover
              ></v-img>
            </v-col>
          </v-row>
        </v-container>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tab = ref(null)
</script>

<script>
  export default {
    data: () => ({
      tab: null,
    }),
  }
</script>

```

# Vuetify component v-tabs - prop align tabs center

Example code

```vue
<template>
  <v-card>
    <v-tabs
      v-model="tab"
      align-tabs="center"
      color="deep-purple-accent-4"
    >
      <v-tab :value="1">Landscape</v-tab>
      <v-tab :value="2">City</v-tab>
      <v-tab :value="3">Abstract</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="n in 3"
        :key="n"
        :value="n"
      >
        <v-container fluid>
          <v-row>
            <v-col
              v-for="i in 6"
              :key="i"
              cols="12"
              md="4"
            >
              <v-img
                :lazy-src="`https://picsum.photos/10/6?image=${i * n * 5 + 10}`"
                :src="`https://picsum.photos/500/300?image=${i * n * 5 + 10}`"
                height="205"
                cover
              ></v-img>
            </v-col>
          </v-row>
        </v-container>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tab = ref(null)
</script>

<script>
  export default {
    data: () => ({
      tab: null,
    }),
  }
</script>

```

# Vuetify component v-tabs - prop icons

Example code

```vue
<template>
  <v-sheet elevation="6">
    <v-tabs
      bg-color="indigo"
      next-icon="mdi-arrow-right-bold-box-outline"
      prev-icon="mdi-arrow-left-bold-box-outline"
      show-arrows
    >
      <v-tab
        v-for="i in 30"
        :key="i"
        :text="`Item ${i}`"
      ></v-tab>
    </v-tabs>
  </v-sheet>
</template>

```

# Vuetify component v-tabs - misc overflow to menu

Example code

```vue
<template>
  <v-card>
    <v-toolbar
      color="deep-purple-accent-4"
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Page title</v-toolbar-title>

      <v-btn icon="mdi-magnify"></v-btn>

      <v-btn icon="mdi-dots-vertical"></v-btn>

      <template v-slot:extension>
        <v-tabs
          v-model="currentItem"
          fixed-tabs
        >
          <v-tab
            v-for="item in items"
            :key="item"
            :text="item"
            :value="'tab-' + item"
          ></v-tab>

          <v-menu v-if="more.length">
            <template v-slot:activator="{ props }">
              <v-btn
                class="align-self-center me-4"
                height="100%"
                rounded="0"
                variant="plain"
                v-bind="props"
              >
                more

                <v-icon icon="mdi-menu-down" end></v-icon>
              </v-btn>
            </template>

            <v-list class="bg-grey-lighten-3">
              <v-list-item
                v-for="item in more"
                :key="item"
                :title="item"
                @click="addItem(item)"
              ></v-list-item>
            </v-list>
          </v-menu>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-window v-model="currentItem">
      <v-tabs-window-item
        v-for="item in items.concat(more)"
        :key="item"
        :value="'tab-' + item"
      >
        <v-card flat>
          <v-card-text>
            <h2>{{ item }}</h2>
            {{ text }}
          </v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { nextTick, ref } from 'vue'

  const text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

  const currentItem = ref('tab-Web')
  const items = ref([
    'Web',
    'Shopping',
    'Videos',
    'Images',
  ])
  const more = ref([
    'News',
    'Maps',
    'Books',
    'Flights',
    'Apps',
  ])

  function addItem (item) {
    const removed = items.value.splice(0, 1)
    items.value.push(...more.value.splice(more.value.indexOf(item), 1))
    more.value.push(...removed)
    nextTick(() => { currentItem.value = 'tab-' + item })
  }
</script>

<script>
  export default {
    data: () => ({
      currentItem: 'tab-Web',
      items: [
        'Web', 'Shopping', 'Videos', 'Images',
      ],
      more: [
        'News', 'Maps', 'Books', 'Flights', 'Apps',
      ],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }),

    methods: {
      addItem (item) {
        const removed = this.items.splice(0, 1)
        this.items.push(
          ...this.more.splice(this.more.indexOf(item), 1),
        )
        this.more.push(...removed)
        this.$nextTick(() => { this.currentItem = 'tab-' + item })
      },
    },
  }
</script>

```

# Vuetify component v-tabs - prop fixed tabs

Example code

```vue
<template>
  <v-tabs
    bg-color="indigo-darken-2"
    fixed-tabs
  >
    <v-tab text="Option"></v-tab>

    <v-tab text="Another Option"></v-tab>
  </v-tabs>
</template>

```

# Vuetify component v-tabs - misc tab items

Example code

```vue
<template>
  <v-card>
    <v-tabs
      v-model="tab"
      bg-color="primary"
    >
      <v-tab
        v-for="item in items"
        :key="item.tab"
        :title="item.tab"
      ></v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="item in items"
        :key="item.tab"
      >
        <v-card flat>
          <v-card-text>{{ item.content }}</v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const items = [
    { tab: 'One', content: 'Tab 1 Content' },
    { tab: 'Two', content: 'Tab 2 Content' },
    { tab: 'Three', content: 'Tab 3 Content' },
    { tab: 'Four', content: 'Tab 4 Content' },
    { tab: 'Five', content: 'Tab 5 Content' },
    { tab: 'Six', content: 'Tab 6 Content' },
    { tab: 'Seven', content: 'Tab 7 Content' },
    { tab: 'Eight', content: 'Tab 8 Content' },
    { tab: 'Nine', content: 'Tab 9 Content' },
    { tab: 'Ten', content: 'Tab 10 Content' },
  ]

  const tab = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        tab: null,
        items: [
          { tab: 'One', content: 'Tab 1 Content' },
          { tab: 'Two', content: 'Tab 2 Content' },
          { tab: 'Three', content: 'Tab 3 Content' },
          { tab: 'Four', content: 'Tab 4 Content' },
          { tab: 'Five', content: 'Tab 5 Content' },
          { tab: 'Six', content: 'Tab 6 Content' },
          { tab: 'Seven', content: 'Tab 7 Content' },
          { tab: 'Eight', content: 'Tab 8 Content' },
          { tab: 'Nine', content: 'Tab 9 Content' },
          { tab: 'Ten', content: 'Tab 10 Content' },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-tabs - misc mobile

Example code

```vue
<template>
  <v-card class="mx-auto" width="350px">
    <v-toolbar color="surface">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Contacts</v-toolbar-title>

      <v-btn icon="mdi-magnify"></v-btn>

      <v-btn icon="mdi-dots-vertical"></v-btn>

      <template v-slot:extension>
        <v-tabs
          v-model="tabs"
          color="primary"
          grow
        >
          <v-tab
            :value="1"
          >
            <v-icon icon="mdi-phone"></v-icon>
          </v-tab>

          <v-tab
            :value="2"
          >
            <v-icon icon="mdi-heart"></v-icon>
          </v-tab>

          <v-tab
            :value="3"
          >
            <v-icon icon="mdi-account-box"></v-icon>
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-window v-model="tabs">
      <v-tabs-window-item
        v-for="i in 3"
        :key="i"
        :value="i"
      >
        <v-card>
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          </v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tabs = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        tabs: null,
      }
    },
  }
</script>

```

# Vuetify component v-tabs - prop grow

Example code

```vue
<template>
  <v-card color="basil">
    <v-card-title class="text-center justify-center py-6">
      <h1 class="font-weight-bold text-h2 text-basil">
        BASiL
      </h1>
    </v-card-title>

    <v-tabs
      v-model="tab"
      bg-color="transparent"
      color="basil"
      grow
    >
      <v-tab
        v-for="item in items"
        :key="item"
        :text="item"
        :value="item"
      ></v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="item in items"
        :key="item"
        :value="item"
      >
        <v-card
          color="basil"
          flat
        >
          <v-card-text>{{ text }}</v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const tab = ref('Appetizers')

  const items = [
    'Appetizers',
    'Entrees',
    'Deserts',
    'Cocktails',
  ]
  const text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
</script>

<script>
  export default {
    data () {
      return {
        tab: 'Appetizers',
        items: [
          'Appetizers', 'Entrees', 'Deserts', 'Cocktails',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>

<style>
/* Helper classes */
.bg-basil {
  background-color: #FFFBE6 !important;
}
.text-basil {
  color: #356859 !important;
}
</style>

```

# Vuetify component v-tabs - misc pagination

Example code

```vue
<template>
  <v-card>
    <v-tabs
      bg-color="teal-darken-3"
      slider-color="teal-lighten-3"
      show-arrows
    >
      <v-tab
        v-for="i in 30"
        :key="i"
        :text="'Item ' + i"
        :value="'tab-' + i"
      ></v-tab>
    </v-tabs>
  </v-card>
</template>

```

# Vuetify component v-tabs - slot tabs

Example code

```vue
<template>
  <v-sheet color="#0d1117" elevation="3" rounded="lg">
    <v-tabs
      v-model="tab"
      :items="tabs"
      align-tabs="center"
      color="white"
      height="60"
      slider-color="#f78166"
    >
      <template v-slot:tab="{ item }">
        <v-tab
          :prepend-icon="item.icon"
          :text="item.text"
          :value="item.value"
          class="text-none"
        ></v-tab>
      </template>

      <template v-slot:item="{ item }">
        <v-tabs-window-item :value="item.value" class="pa-4">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </v-tabs-window-item>
      </template>
    </v-tabs>
  </v-sheet>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const tab = shallowRef('tab-1')
  const tabs = [
    {
      icon: 'mdi-book-open-page-variant',
      text: 'Readme',
      value: 'tab-1',
    },
    {
      icon: 'mdi-handshake-outline',
      text: 'Code of Conduct',
      value: 'tab-2',
    },
    {
      icon: 'mdi-license',
      text: 'MIT License',
      value: 'tab-3',
    },
    {
      icon: 'mdi-shield-lock-outline',
      text: 'Security',
      value: 'tab-4',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      tab: 'tab-1',
      tabs: [
        {
          icon: 'mdi-book-open-page-variant',
          text: 'Readme',
          value: 'tab-1',
        },
        {
          icon: 'mdi-handshake-outline',
          text: 'Code of Conduct',
          value: 'tab-2',
        },
        {
          icon: 'mdi-license',
          text: 'MIT License',
          value: 'tab-3',
        },
        {
          icon: 'mdi-shield-lock-outline',
          text: 'Security',
          value: 'tab-4',
        },
      ],
    }),
  }
</script>

```
