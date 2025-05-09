# Vuetify component v-chip - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="text-center">
      <v-chip v-bind="props" v-model="chipModel">
        Chip
      </v-chip>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="prepend" label="Prepend icon"></v-checkbox>
      <v-checkbox v-model="append" label="Append icon"></v-checkbox>
      <v-checkbox v-model="closable" label="Closable">
        <template v-slot:append>
          <v-fade-transition>
            <v-btn v-if="!chipModel" variant="plain" @click="chipModel = true">Reset</v-btn>
          </v-fade-transition>
        </template>
      </v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const variants = ['outlined', 'elevated', 'text', 'plain']
  const name = 'v-chip'
  const model = ref('default')
  const options = [...variants]
  const block = ref(false)
  const stacked = ref(false)
  const prepend = ref(false)
  const append = ref(false)
  const closable = ref(false)
  const props = computed(() => {
    return {
      block: block.value || undefined,
      closable: closable.value || undefined,
      stacked: stacked.value || undefined,
      'prepend-icon': prepend.value ? '$vuetify' : undefined,
      'append-icon': append.value ? '$vuetify' : undefined,
      variant: variants.includes(model.value) ? model.value : undefined,
    }
  })

  const chipModel = ref(true)

  watch(stacked, val => val && (prepend.value = true))

  const slots = computed(() => {
    return `
  Chip
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-chip - prop filter

Example code

```vue
<template>
  <v-row
    align="center"
    justify="space-around"
  >
    <v-chip
      :model-value="active"
      class="ma-2"
      filter
    >
      I'm v-chip
    </v-chip>

    <v-chip
      :model-value="active"
      class="ma-2"
      filter-icon="mdi-plus"
      filter
    >
      I'm v-chip
    </v-chip>

    <v-chip
      :model-value="active"
      class="ma-2"
      filter-icon="mdi-minus"
      filter
    >
      I'm v-chip
    </v-chip>

    <v-switch
      v-model="active"
      label="Active"
    ></v-switch>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const active = ref(false)
</script>

<script>
  export default {
    data: () => ({
      active: false,
    }),
  }
</script>

```

# Vuetify component v-chip - prop colored

Example code

```vue
<template>
  <div class="d-flex justify-center ga-2">
    <v-chip>
      Default
    </v-chip>

    <v-chip color="primary">
      Primary
    </v-chip>

    <v-chip color="secondary">
      Secondary
    </v-chip>

    <v-chip color="red">
      Red
    </v-chip>

    <v-chip color="green">
      Green
    </v-chip>
  </div>
  <div class="d-flex justify-center ga-2 mt-2">
    <v-chip variant="flat">
      Default flat
    </v-chip>

    <v-chip color="primary" variant="flat">
      Primary flat
    </v-chip>

    <v-chip color="secondary" variant="flat">
      Secondary flat
    </v-chip>

    <v-chip color="red" variant="flat">
      Red flat
    </v-chip>

    <v-chip color="green" variant="flat">
      Green flat
    </v-chip>
  </div>
</template>
<script setup lang="ts">
</script>

```

# Vuetify component v-chip - slot icon

Example code

```vue
<template>
  <div class="text-center">
    <v-chip
      class="ma-2"
      color="indigo"
      prepend-icon="mdi-account-circle"
    >
      Mike
    </v-chip>

    <v-chip
      append-icon="mdi-star"
      class="ma-2"
      color="orange"
    >
      Premium
    </v-chip>

    <v-chip
      append-icon="mdi-cake-variant"
      class="ma-2"
      color="primary"
    >
      1 Year
    </v-chip>

    <v-chip
      class="ma-2"
      color="green"
    >
      <template v-slot:prepend>
        <v-avatar
          class="green-darken-4"
        >
          1
        </v-avatar>
      </template>
      Years
    </v-chip>

    <v-chip
      :model-value="true"
      class="ma-2"
      color="teal"
      prepend-icon="mdi-checkbox-marked-circle"
      closable
    >
      Confirmed
    </v-chip>

    <v-chip
      :model-value="true"
      class="ma-2"
      close-icon="mdi-delete"
      color="teal"
      prepend-icon="mdi-checkbox-marked-circle"
      closable
    >
      Confirmed
    </v-chip>
  </div>
</template>

```

# Vuetify component v-chip - prop closable

Example code

```vue
<template>
  <div class="text-center">
    <v-chip
      v-if="chip"
      class="ma-2"
      closable
      @click:close="chip = false"
    >
      Closable
    </v-chip>

    <v-btn
      v-if="!chip"
      color="primary"
      @click="chip = true"
    >
      Reset Chip
    </v-btn>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const chip = ref(true)
</script>

<script>
  export default {
    data () {
      return {
        chip: true,
      }
    },
  }
</script>

```

# Vuetify component v-chip - prop no ripple

Example code

```vue
<template>
  <div class="text-center">
    <v-chip :ripple="false" link>
      Default
    </v-chip>
  </div>
</template>

```

# Vuetify component v-chip - prop sizes

Example code

```vue
<template>
  <div class="d-flex justify-center align-center ga-2">
    <v-label style="width: 100px">default</v-label>

    <v-chip size="x-small">
      x-small
    </v-chip>

    <v-chip size="small">
      small
    </v-chip>

    <v-chip>
      default
    </v-chip>

    <v-chip size="large">
      large
    </v-chip>

    <v-chip size="x-large">
      x-large
    </v-chip>
  </div>
  <div class="d-flex justify-center align-center ga-2 mt-2">
    <v-label style="width: 100px">comfortable</v-label>

    <v-chip density="comfortable" size="x-small">
      x-small
    </v-chip>

    <v-chip density="comfortable" size="small">
      small
    </v-chip>

    <v-chip density="comfortable">
      default
    </v-chip>

    <v-chip density="comfortable" size="large">
      large
    </v-chip>

    <v-chip density="comfortable" size="x-large">
      x-large
    </v-chip>
  </div>
  <div class="d-flex justify-center align-center ga-2 mt-2">
    <v-label style="width: 100px">compact</v-label>

    <v-chip density="compact" size="x-small">
      x-small
    </v-chip>

    <v-chip density="compact" size="small">
      small
    </v-chip>

    <v-chip density="compact">
      default
    </v-chip>

    <v-chip density="compact" size="large">
      large
    </v-chip>

    <v-chip density="compact" size="x-large">
      x-large
    </v-chip>
  </div>
</template>
<script setup lang="ts">
</script>

```

# Vuetify component v-chip - prop label

Example code

```vue
<template>
  <div class="text-center">
    <v-chip
      class="ma-2"
      label
    >
      Label
    </v-chip>

    <v-chip
      class="ma-2"
      color="pink"
      label
    >
      <v-icon icon="mdi-label" start></v-icon>
      Tags
    </v-chip>

    <v-chip
      class="ma-2"
      color="primary"
      label
    >
      <v-icon icon="mdi-account-circle-outline" start></v-icon>
      John Leider
    </v-chip>

    <v-chip
      class="ma-2"
      color="cyan"
      closable
      label
    >
      <v-icon icon="mdi-twitter" start></v-icon>
      New Tweets
    </v-chip>
  </div>
</template>

```

# Vuetify component v-chip - prop outlined

Example code

```vue
<template>
  <div class="text-center">
    <v-chip
      class="ma-2"
      color="success"
      variant="outlined"
    >
      <v-icon icon="mdi-server-plus" start></v-icon>
      Server Status
    </v-chip>

    <v-chip
      class="ma-2"
      color="primary"
      variant="outlined"
    >
      User Account
      <v-icon icon="mdi-account-outline" end></v-icon>
    </v-chip>
  </div>
</template>

```

# Vuetify component v-chip - misc custom list

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-toolbar
      color="transparent"
      flat
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Photo Info</v-toolbar-title>

      <v-btn
        icon="mdi-magnify"
        @click="searchField.focus()"
      >
      </v-btn>
    </v-toolbar>

    <v-container>
      <v-row
        align="center"
        justify="start"
      >
        <v-col
          v-for="(selection, i) in selections"
          :key="selection.text"
          class="py-1 pe-0"
          cols="auto"
        >
          <v-chip
            :disabled="loading"
            closable
            @click:close="selected.splice(i, 1)"
          >
            <v-icon
              :icon="selection.icon"
              start
            ></v-icon>

            {{ selection.text }}
          </v-chip>
        </v-col>

        <v-col
          v-if="!allSelected"
          cols="12"
        >
          <v-text-field
            ref="searchField"
            v-model="search"
            label="Search"
            hide-details
            single-line
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>

    <v-divider v-if="!allSelected"></v-divider>

    <v-list>
      <template v-for="item in categories">
        <v-list-item
          v-if="!selected.includes(item)"
          :key="item.text"
          :disabled="loading"
          @click="selected.push(item)"
        >
          <template v-slot:prepend>
            <v-icon
              :disabled="loading"
              :icon="item.icon"
            ></v-icon>
          </template>

          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item>
      </template>
    </v-list>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        :disabled="!selected.length"
        :loading="loading"
        color="purple"
        variant="text"
        @click="next"
      >
        Next
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { computed, ref, watch } from 'vue'

  const items = [
    {
      text: 'Nature',
      icon: 'mdi-nature',
    },
    {
      text: 'Nightlife',
      icon: 'mdi-glass-wine',
    },
    {
      text: 'November',
      icon: 'mdi-calendar-range',
    },
    {
      text: 'Portland',
      icon: 'mdi-map-marker',
    },
    {
      text: 'Biking',
      icon: 'mdi-bike',
    },
  ]
  const searchField = ref()

  const loading = ref(false)
  const search = ref('')
  const selected = ref([])

  const allSelected = computed(() => {
    return selected.value.length === items.length
  })
  const categories = computed(() => {
    const _search = search.value.toLowerCase()
    if (!_search) return items
    return items.filter(item => {
      const text = item.text.toLowerCase()
      return text.indexOf(_search) > -1
    })
  })
  const selections = computed(() => {
    const selections = []
    for (const selection of selected.value) {
      selections.push(selection)
    }
    return selections
  })

  watch(selected, () => {
    search.value = ''
  })

  function next () {
    loading.value = true
    setTimeout(() => {
      search.value = ''
      selected.value = []
      loading.value = false
    }, 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          text: 'Nature',
          icon: 'mdi-nature',
        },
        {
          text: 'Nightlife',
          icon: 'mdi-glass-wine',
        },
        {
          text: 'November',
          icon: 'mdi-calendar-range',
        },
        {
          text: 'Portland',
          icon: 'mdi-map-marker',
        },
        {
          text: 'Biking',
          icon: 'mdi-bike',
        },
      ],
      loading: false,
      search: '',
      selected: [],
    }),

    computed: {
      allSelected () {
        return this.selected.length === this.items.length
      },
      categories () {
        const search = this.search.toLowerCase()

        if (!search) return this.items

        return this.items.filter(item => {
          const text = item.text.toLowerCase()

          return text.indexOf(search) > -1
        })
      },
      selections () {
        const selections = []

        for (const selection of this.selected) {
          selections.push(selection)
        }

        return selections
      },
    },

    watch: {
      selected () {
        this.search = ''
      },
    },

    methods: {
      next () {
        this.loading = true

        setTimeout(() => {
          this.search = ''
          this.selected = []
          this.loading = false
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-chip - misc expandable

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-row
      align="center"
      class="pa-6"
    >
      <span class="me-4">To</span>

      <v-menu
        v-model="menu"
        location="top start"
        origin="top start"
        transition="scale-transition"
      >
        <template v-slot:activator="{ props }">
          <v-chip
            v-bind="props"
            link
            pill
          >
            <v-avatar start>
              <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
            </v-avatar>

            John Leider
          </v-chip>
        </template>

        <v-card width="300">
          <v-list bg-color="black">
            <v-list-item>
              <template v-slot:prepend>
                <v-avatar image="https://cdn.vuetifyjs.com/images/john.png"></v-avatar>
              </template>

              <v-list-item-title>John Leider</v-list-item-title>

              <v-list-item-subtitle>john@google.com</v-list-item-subtitle>

              <template v-slot:append>
                <v-list-item-action>
                  <v-btn
                    variant="text"
                    icon
                    @click="menu = false"
                  >
                    <v-icon>mdi-close-circle</v-icon>
                  </v-btn>
                </v-list-item-action>
              </template>
            </v-list-item>
          </v-list>

          <v-list>
            <v-list-item prepend-icon="mdi-briefcase" link>
              <v-list-item-subtitle>john@gmail.com</v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-card>
      </v-menu>
    </v-row>

    <v-divider></v-divider>

    <div class="pa-3">
      <v-text-field
        label="Subject"
        model-value="Re: Vacation Request"
        variant="underlined"
        single-line
      ></v-text-field>

      <v-textarea
        label="Message"
        variant="underlined"
        single-line
      ></v-textarea>
    </div>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const menu = ref(false)
</script>

<script>
  export default {
    data: () => ({
      menu: false,
    }),
  }
</script>

```

# Vuetify component v-chip - prop draggable

Example code

```vue
<template>
  <div class="text-center">
    <v-chip draggable>
      Default
    </v-chip>
  </div>
</template>

```

# Vuetify component v-chip - event action chips

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="450"
  >
    <v-img
      :aspect-ratio="16/9"
      src="https://cdn.vuetifyjs.com/images/cards/house.jpg"
      cover
    >
    </v-img>
    <v-card-title class="flex-column align-start">
      <div class="text-h4 mb-2">
        Welcome Home...
      </div>
      <div class="text-h6 font-weight-regular text-grey">
        Monday, 12:30 PM, Mostly Sunny
      </div>
      <div class="d-flex align-center">
        <v-avatar
          class="me-4"
          size="24"
        >
          <v-img src="https://cdn.vuetifyjs.com/images/weather/part-cloud-48px.png"></v-img>
        </v-avatar>

        <span class="text-body-2 text-grey">81° / 62°</span>
      </div>
    </v-card-title>

    <v-divider class="mx-4"></v-divider>

    <v-card-text class="d-flex justify-space-between">
      <v-chip
        prepend-icon="mdi-brightness-5"
        @click="lights"
      >
        Turn on lights
      </v-chip>
      <v-chip
        prepend-icon="mdi-alarm-check"
        @click="alarm"
      >
        Set alarm
      </v-chip>
      <v-chip
        icon="mdi-blinds"
        @click="blinds"
      >
        Close blinds
      </v-chip>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    methods: {
      alarm () {
        alert('Turning on alarm...')
      },
      blinds () {
        alert('Toggling blinds...')
      },
      lights () {
        alert('Toggling lights...')
      },
    },
  }
</script>

```

# Vuetify component v-chip - misc in selects

Example code

```vue
<template>
  <v-combobox
    v-model="chips"
    :items="items"
    label="Your favorite hobbies"
    prepend-icon="mdi-filter-variant"
    variant="solo"
    chips
    clearable
    closable-chips
    multiple
  >
    <template v-slot:chip="{ props, item }">
      <v-chip v-bind="props">
        <strong>{{ item.raw }}</strong>&nbsp;
        <span>(interest)</span>
      </v-chip>
    </template>
  </v-combobox>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ['Streaming', 'Eating']

  const chips = ref(['Programming', 'Playing video games', 'Watching movies', 'Sleeping'])
</script>

<script>
  export default {
    data () {
      return {
        chips: ['Programming', 'Playing video games', 'Watching movies', 'Sleeping'],
        items: ['Streaming', 'Eating'],
      }
    },
  }
</script>

```

# Vuetify component v-chip - misc filtering

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="450"
  >
    <v-toolbar
      color="primary"
      height="88"
      flat
    >
      <template v-slot:prepend>
        <v-btn icon="mdi-arrow-left">
        </v-btn>
      </template>

      <v-text-field
        v-model="search"
        label="Search News"
        prepend-inner-icon="mdi-magnify"
        clearable
        hide-details
        single-line
      ></v-text-field>

      <template v-slot:append>
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-toolbar>

    <div v-if="keywords.length > 0" class="py-3 px-4">
      <v-chip
        v-for="(keyword, i) in keywords"
        :key="i"
        class="me-2"
      >
        {{ keyword }}
      </v-chip>

    </div>

    <v-divider></v-divider>

    <v-list lines="three">
      <v-list-item
        v-for="(item, i) in searching"
        :key="i"
        link
      >
        <template v-slot:prepend>
          <v-avatar
            class="me-4 mt-2"
            rounded="0"
          >
            <v-img :src="item.image" cover></v-img>
          </v-avatar>
        </template>

        <v-list-item-title
          class="text-uppercase font-weight-regular text-caption"
          v-text="item.category"
        ></v-list-item-title>

        <div v-text="item.title"></div>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const items = [
    {
      image: 'https://cdn.vuetifyjs.com/docs/images/chips/globe.png',
      title: 'TBI\u2019s 5 Best: SF Mocktails to Finish Dry January Strong',
      category: 'Travel',
      keyword: 'Drinks',
    },
    {
      image: 'https://cdn.vuetifyjs.com/docs/images/chips/cpu.png',
      title: 'PWAs on iOS 12.2 beta: the good, the bad, and the \u201Cnot sure yet if good\u201D',
      category: 'Technology',
      keyword: 'Phones',
    },
    {
      image: 'https://cdn.vuetifyjs.com/docs/images/chips/rocket.png',
      title: 'How to Get Media Mentions for Your Business',
      category: 'Media',
      keyword: 'Social',
    },
    {
      image: 'https://cdn.vuetifyjs.com/docs/images/chips/bulb.png',
      title: 'The Pitfalls Of Outsourcing Self-Awareness To Artificial Intelligence',
      category: 'Technology',
      keyword: 'Military',
    },
    {
      image: 'https://cdn.vuetifyjs.com/docs/images/chips/raft.png',
      title: 'Degrees of Freedom and Sudoko',
      category: 'Travel',
      keyword: 'Social',
    },
  ]

  const search = ref('')

  const keywords = computed(() => {
    if (!search.value) return []

    const keywords = []

    for (const search of searching.value) {
      keywords.push(search.keyword)
    }

    return keywords
  })
  const searching = computed(() => {
    if (!search.value) return items

    const _search = search.value.toLowerCase()

    return items.filter(item => {
      const text = item.title.toLowerCase()
      return text.indexOf(_search) > -1
    })
  })
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          image: 'https://cdn.vuetifyjs.com/docs/images/chips/globe.png',
          title: 'TBI’s 5 Best: SF Mocktails to Finish Dry January Strong',
          category: 'Travel',
          keyword: 'Drinks',

        },
        {
          image: 'https://cdn.vuetifyjs.com/docs/images/chips/cpu.png',
          title: 'PWAs on iOS 12.2 beta: the good, the bad, and the “not sure yet if good”',
          category: 'Technology',
          keyword: 'Phones',
        },
        {
          image: 'https://cdn.vuetifyjs.com/docs/images/chips/rocket.png',
          title: 'How to Get Media Mentions for Your Business',
          category: 'Media',
          keyword: 'Social',
        },
        {
          image: 'https://cdn.vuetifyjs.com/docs/images/chips/bulb.png',
          title: 'The Pitfalls Of Outsourcing Self-Awareness To Artificial Intelligence',
          category: 'Technology',
          keyword: 'Military',
        },
        {
          image: 'https://cdn.vuetifyjs.com/docs/images/chips/raft.png',
          title: 'Degrees of Freedom and Sudoko',
          category: 'Travel',
          keyword: 'Social',
        },
      ],
      search: '',
    }),

    computed: {
      keywords () {
        if (!this.search) return []

        const keywords = []

        for (const search of this.searching) {
          keywords.push(search.keyword)
        }

        return keywords
      },
      searching () {
        if (!this.search) return this.items

        const search = this.search.toLowerCase()

        return this.items.filter(item => {
          const text = item.title.toLowerCase()

          return text.indexOf(search) > -1
        })
      },
    },
  }
</script>

```
