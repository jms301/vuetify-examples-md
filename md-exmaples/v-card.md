# Vuetify component v-card - usage

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

      <v-card v-bind="props">
        <template v-slot:text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </template>

        <v-card-actions v-if="actions">
          <v-btn>Click me</v-btn>
        </v-card-actions>
      </v-card>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="title" label="Show title"></v-checkbox>

      <v-checkbox v-model="subtitle" label="Show subtitle"></v-checkbox>

      <v-checkbox v-model="actions" label="Show actions"></v-checkbox>

      <v-checkbox v-model="loading" label="Loading"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-card'
  const model = ref('default')
  const actions = ref(false)
  const loading = ref(false)
  const subtitle = ref(false)
  const title = ref(false)
  const options = ['outlined', 'tonal']
  const props = computed(() => {
    return {
      loading: loading.value || undefined,
      title: title.value ? 'Card title' : undefined,
      subtitle: subtitle.value ? 'Subtitle' : undefined,
      text: '...',
      variant: ['outlined', 'tonal'].includes(model.value) ? model.value : undefined,
    }
  })

  const slots = computed(() => {
    let str = ''

    if (actions.value) {
      str += `
  <v-card-actions>
    <v-btn>Click me</v-btn>
  </v-card-actions>
`
    }

    return str
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-card - prop variant

Example code

```vue
<template>
  <v-row dense>
    <v-col
      v-for="(variant, i) in variants"
      :key="i"
      cols="12"
      md="4"
    >
      <v-card
        :variant="variant"
        class="mx-auto"
        color="surface-variant"
        max-width="344"
        subtitle="Greyhound divisely hello coldly fonwderfully"
        title="Headline"
      >
        <template v-slot:actions>
          <v-btn text="Button"></v-btn>
        </template>
      </v-card>

      <div class="text-center text-caption">{{ variant }}</div>
    </v-col>
  </v-row>
</template>

<script setup>
  const variants = ['elevated', 'flat', 'tonal', 'outlined', 'text', 'plain']
</script>

<script>
  export default {
    data: () => ({
      variants: ['elevated', 'flat', 'tonal', 'outlined', 'text', 'plain'],
    }),
  }
</script>

```

# Vuetify component v-card - misc grids

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card>
            <v-img
              :src="card.src"
              class="align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
              cover
            >
              <v-card-title class="text-white" v-text="card.title"></v-card-title>
            </v-img>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                color="medium-emphasis"
                icon="mdi-heart"
                size="small"
              ></v-btn>

              <v-btn
                color="medium-emphasis"
                icon="mdi-bookmark"
                size="small"
              ></v-btn>

              <v-btn
                color="medium-emphasis"
                icon="mdi-share-variant"
                size="small"
              ></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
  const cards = [
    { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
    { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
    { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
  ]
</script>

<script>
  export default {
    data: () => ({
      cards: [
        { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
    }),
  }
</script>

```

# Vuetify component v-card - prop loading

Example code

```vue
<template>
  <v-card
    :disabled="loading"
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <template v-slot:loader="{ isActive }">
      <v-progress-linear
        :active="isActive"
        color="deep-purple"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      cover
    ></v-img>

    <v-card-item>
      <v-card-title>Cafe Badilico</v-card-title>

      <v-card-subtitle>
        <span class="me-1">Local Favorite</span>

        <v-icon
          color="error"
          icon="mdi-fire-circle"
          size="small"
        ></v-icon>
      </v-card-subtitle>
    </v-card-item>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :model-value="4.5"
          color="amber"
          density="compact"
          size="small"
          half-increments
          readonly
        ></v-rating>

        <div class="text-grey ms-4">
          4.5 (413)
        </div>
      </v-row>

      <div class="my-4 text-subtitle-1">
        $ • Italian, Cafe
      </div>

      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>

    <v-divider class="mx-4 mb-1"></v-divider>

    <v-card-title>Tonight's availability</v-card-title>

    <div class="px-4 mb-2">
      <v-chip-group v-model="selection" selected-class="bg-deep-purple-lighten-2">
        <v-chip>5:30PM</v-chip>

        <v-chip>7:30PM</v-chip>

        <v-chip>8:00PM</v-chip>

        <v-chip>9:00PM</v-chip>
      </v-chip-group>
    </div>

    <v-card-actions>
      <v-btn
        color="deep-purple-lighten-2"
        text="Reserve"
        block
        border
        @click="reserve"
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const loading = ref(false)
  const selection = ref(1)
  function reserve () {
    loading.value = true
    setTimeout(() => (loading.value = false), 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      loading: false,
      selection: 1,
    }),

    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
    },
  }
</script>

```

# Vuetify component v-card - misc information card

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-text>
      <div>Word of the Day</div>

      <p class="text-h4 font-weight-black">be•nev•o•lent</p>

      <p>adjective</p>

      <div class="text-medium-emphasis">
        well meaning and kindly.<br>
        "a benevolent smile"
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple-accent-4"
        text="Learn More"
        variant="text"
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-card - misc card reveal

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-text>
      <div>Word of the Day</div>

      <p class="text-h4 font-weight-black">el·ee·mos·y·nar·y</p>

      <p>adjective</p>

      <div class="text-medium-emphasis">
        relating to or dependent on charity; charitable; charitable donations. Pertaining to alms.<br>
        "an eleemosynary educational institution."
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="teal-accent-4"
        text="Learn More"
        variant="text"
        @click="reveal = true"
      ></v-btn>
    </v-card-actions>

    <v-expand-transition>
      <v-card
        v-if="reveal"
        class="position-absolute w-100"
        height="100%"
        style="bottom: 0;"
      >
        <v-card-text class="pb-0">
          <p class="text-h4">Origin</p>

          <p class="text-medium-emphasis">
            late 16th century (as a noun denoting a place where alms were distributed): from medieval Latin eleemosynarius, from late Latin eleemosyna ‘alms’, from Greek eleēmosunē ‘compassion’
          </p>
        </v-card-text>

        <v-card-actions class="pt-0">
          <v-btn
            color="teal-accent-4"
            text="Close"
            variant="text"
            @click="reveal = false"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-expand-transition>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const reveal = ref(false)
</script>

<script>
  export default {
    data: () => ({
      reveal: false,
    }),
  }
</script>

```

# Vuetify component v-card - misc media with text

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="align-end text-white"
      height="200"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
      cover
    >
      <v-card-title>Top 10 Australian beaches</v-card-title>
    </v-img>

    <v-card-subtitle class="pt-4">
      Number 10
    </v-card-subtitle>

    <v-card-text>
      <div>Whitehaven Beach</div>

      <div>Whitsunday Island, Whitsunday Islands</div>
    </v-card-text>

    <v-card-actions>
      <v-btn color="orange" text="Share"></v-btn>

      <v-btn color="orange" text="Explore"></v-btn>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-card - misc earnings goal

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="500" border flat>
    <v-list-item class="px-6" height="88">
      <template v-slot:prepend>
        <v-avatar color="surface-light" size="32">🎯</v-avatar>
      </template>

      <template v-slot:title> Set an earnings goal. </template>

      <template v-slot:append>
        <v-btn
          class="text-none"
          color="primary"
          text="Create goal"
          variant="text"
          slim
        ></v-btn>
      </template>
    </v-list-item>

    <v-divider></v-divider>

    <v-card-text class="text-medium-emphasis pa-6">
      <div class="text-h6 mb-6">Earn my first $100</div>

      <div class="text-h4 font-weight-black mb-4">0%</div>

      <v-progress-linear
        bg-color="surface-variant"
        class="mb-6"
        color="primary"
        height="10"
        model-value="2"
        rounded="pill"
      ></v-progress-linear>

      <div>$0 of $100 earned — 7 days left</div>
    </v-card-text>
  </v-card>
</template>

```

# Vuetify component v-card - prop elevation

Example code

```vue
<template>
  <v-card
    class="mx-auto my-8"
    elevation="16"
    max-width="344"
  >
    <v-card-item>
      <v-card-title>
        Card title
      </v-card-title>

      <v-card-subtitle>
        Card subtitle secondary text
      </v-card-subtitle>
    </v-card-item>

    <v-card-text>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    </v-card-text>
  </v-card>
</template>

```

# Vuetify component v-card - prop elevated

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
    variant="elevated"
  >
    <v-card-item>
      <div>
        <div class="text-overline mb-1">
          OVERLINE
        </div>

        <div class="text-h6 mb-1">
          Headline
        </div>

        <div class="text-caption">Greyhound divisely hello coldly fonwderfully</div>
      </div>
    </v-card-item>

    <v-card-actions>
      <v-btn text="Button" variant="outlined">

      </v-btn>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-card - misc intermediate

Example code

```vue
<template>
  <v-card class="d-inline-block mx-auto">
    <v-container>
      <v-row justify="space-between">
        <v-col cols="auto">
          <v-img
            height="200"
            src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
            width="200"
          ></v-img>
        </v-col>

        <v-col
          class="text-center ps-0"
          cols="auto"
        >
          <v-row
            class="flex-column ma-0 fill-height"
            justify="center"
          >
            <v-col class="px-0">
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
            </v-col>

            <v-col class="px-0">
              <v-btn icon>
                <v-icon>mdi-bookmark</v-icon>
              </v-btn>
            </v-col>

            <v-col class="px-0">
              <v-btn icon>
                <v-icon>mdi-share-variant</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

```

# Vuetify component v-card - prop image

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="surface-variant"
    image="https://cdn.vuetifyjs.com/docs/images/cards/dark-beach.jpg"
    max-width="340"
    subtitle="Take a walk down the beach"
    title="Evening sunset"
  >
    <template v-slot:actions>
      <v-btn
        append-icon="mdi-chevron-right"
        color="red-lighten-2"
        text="Book Activity"
        variant="outlined"
        block
      ></v-btn>
    </template>
  </v-card>
</template>

```

# Vuetify component v-card - misc twitter card

Example code

```vue
<template>
  <v-card
    class="mx-auto text-white"
    color="#26c6da"
    max-width="400"
    prepend-icon="mdi-twitter"
    title="Twitter"
  >
    <template v-slot:prepend>
      <v-icon size="x-large"></v-icon>
    </template>

    <v-card-text class="text-h5 py-2">
      "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
    </v-card-text>

    <v-card-actions>
      <v-list-item class="w-100">
        <template v-slot:prepend>
          <v-avatar
            color="grey-darken-3"
            image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
          ></v-avatar>
        </template>

        <v-list-item-title>Evan You</v-list-item-title>

        <v-list-item-subtitle>Vue Creator</v-list-item-subtitle>

        <template v-slot:append>
          <div class="justify-self-end">
            <v-icon class="me-1" icon="mdi-heart"></v-icon>
            <span class="subheading me-2">256</span>
            <span class="me-1">·</span>
            <v-icon class="me-1" icon="mdi-share-variant"></v-icon>
            <span class="subheading">45</span>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-card - misc content wrapping

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="400">
    <v-img
      color="surface-variant"
      height="200"
      src="https://cdn.vuetifyjs.com/docs/images/cards/purple-flowers.jpg"
      cover
    >
      <v-toolbar color="transparent">
        <template v-slot:prepend>
          <v-btn icon="$menu"></v-btn>
        </template>

        <v-toolbar-title class="text-h6" text="Messages"></v-toolbar-title>

        <template v-slot:append>
          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
      </v-toolbar>
    </v-img>

    <v-card-text>
      <div class="font-weight-bold ms-1 mb-2">Today</div>

      <v-timeline align="start" density="compact">
        <v-timeline-item
          v-for="message in messages"
          :key="message.time"
          :dot-color="message.color"
          size="x-small"
        >
          <div class="mb-4">
            <div class="font-weight-normal">
              <strong>{{ message.from }}</strong> @{{ message.time }}
            </div>

            <div>{{ message.message }}</div>
          </div>
        </v-timeline-item>
      </v-timeline>
    </v-card-text>
  </v-card>
</template>

<script setup>
  const messages = [
    {
      from: 'You',
      message: `Sure, I'll see you later.`,
      time: '10:42am',
      color: 'deep-purple-lighten-1',
    },
    {
      from: 'John Doe',
      message: 'Yeah, sure. Does 1:00pm work?',
      time: '10:37am',
      color: 'green',
    },
    {
      from: 'You',
      message: 'Did you still want to grab lunch today?',
      time: '9:47am',
      color: 'deep-purple-lighten-1',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      messages: [
        {
          from: 'You',
          message: `Sure, I'll see you later.`,
          time: '10:42am',
          color: 'deep-purple-lighten-1',
        },
        {
          from: 'John Doe',
          message: 'Yeah, sure. Does 1:00pm work?',
          time: '10:37am',
          color: 'green',
        },
        {
          from: 'You',
          message: 'Did you still want to grab lunch today?',
          time: '9:47am',
          color: 'deep-purple-lighten-1',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-card - prop outlined

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
    variant="outlined"
  >
    <v-card-item>
      <div>
        <div class="text-overline mb-1">
          OVERLINE
        </div>

        <div class="text-h6 mb-1">
          Headline
        </div>

        <div class="text-caption">Greyhound divisely hello coldly fonwderfully</div>
      </div>
    </v-card-item>

    <v-card-actions>
      <v-btn text="Button" variant="outlined"></v-btn>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-card - prop hover

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
    hover
  >
    <v-card-item>
      <v-card-title>
        Card title
      </v-card-title>

      <v-card-subtitle>
        Card subtitle secondary text
      </v-card-subtitle>
    </v-card-item>

    <v-card-text>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    </v-card-text>
  </v-card>
</template>

```

# Vuetify component v-card - misc horizontal cards

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-layout>
      <v-system-bar color="pink-darken-2">
        <v-spacer></v-spacer>

        <v-icon>mdi-window-minimize</v-icon>

        <v-icon>mdi-window-maximize</v-icon>

        <v-icon>mdi-close</v-icon>
      </v-system-bar>

      <v-app-bar color="pink">
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>My Music</v-toolbar-title>

        <v-btn icon="mdi-magnify"></v-btn>
      </v-app-bar>

      <v-main>
        <v-container>
          <v-row dense>
            <v-col cols="12">
              <v-card color="#385F73">
                <v-card-title class="text-h5">
                  Unlimited music now
                </v-card-title>

                <v-card-subtitle>
                  Listen to your favorite artists and albums whenever and wherever, online and offline.
                </v-card-subtitle>

                <v-card-actions>
                  <v-btn text="Listen Now" variant="text"></v-btn>
                </v-card-actions>
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-card color="#1F7087">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <div>
                    <v-card-title class="text-h5">
                      Supermodel
                    </v-card-title>

                    <v-card-subtitle>Foster the People</v-card-subtitle>

                    <v-card-actions>
                      <v-btn
                        class="ms-2"
                        size="small"
                        text="START RADIO"
                        variant="outlined"
                      ></v-btn>
                    </v-card-actions>
                  </div>

                  <v-avatar
                    class="ma-3"
                    rounded="0"
                    size="125"
                  >
                    <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"></v-img>
                  </v-avatar>
                </div>
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-card color="#952175">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <div>
                    <v-card-title class="text-h5">
                      Halcyon Days
                    </v-card-title>

                    <v-card-subtitle>Ellie Goulding</v-card-subtitle>

                    <v-card-actions>
                      <v-btn
                        class="ms-2"
                        icon="mdi-play"
                        variant="text"
                      ></v-btn>
                    </v-card-actions>
                  </div>

                  <v-avatar
                    class="ma-3"
                    rounded="0"
                    size="125"
                  >
                    <v-img src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"></v-img>
                  </v-avatar>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

```

# Vuetify component v-card - prop disabled

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
    subtitle="The card stays disabled"
    title="Disabled card"
    disabled
    link
  ></v-card>
</template>

```

# Vuetify component v-card - misc weather card

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="368"
  >
    <v-card-item title="Florida">
      <template v-slot:subtitle>
        <v-icon
          class="me-1 pb-1"
          color="error"
          icon="mdi-alert"
          size="18"
        ></v-icon>

        Extreme Weather Alert
      </template>
    </v-card-item>

    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col
          class="text-h2"
          cols="6"
        >
          64&deg;F
        </v-col>

        <v-col class="text-right" cols="6">
          <v-icon
            color="error"
            icon="mdi-weather-hurricane"
            size="88"
          ></v-icon>
        </v-col>
      </v-row>
    </v-card-text>

    <div class="d-flex py-3 justify-space-between">
      <v-list-item
        density="compact"
        prepend-icon="mdi-weather-windy"
      >
        <v-list-item-subtitle>123 km/h</v-list-item-subtitle>
      </v-list-item>

      <v-list-item
        density="compact"
        prepend-icon="mdi-weather-pouring"
      >
        <v-list-item-subtitle>48%</v-list-item-subtitle>
      </v-list-item>
    </div>

    <v-expand-transition>
      <div v-if="expand">
        <div class="py-2">
          <v-slider
            v-model="time"
            :max="6"
            :step="1"
            :ticks="labels"
            class="mx-4"
            color="primary"
            density="compact"
            show-ticks="always"
            thumb-size="10"
            hide-details
          ></v-slider>
        </div>

        <v-list class="bg-transparent">
          <v-list-item
            v-for="item in forecast"
            :key="item.day"
            :append-icon="item.icon"
            :subtitle="item.temp"
            :title="item.day"
          >
          </v-list-item>
        </v-list>
      </div>
    </v-expand-transition>

    <v-divider></v-divider>

    <v-card-actions>
      <v-btn
        :text="!expand ? 'Full Report' : 'Hide Report'"
        @click="expand = !expand"
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const labels = { 0: 'SU', 1: 'MO', 2: 'TU', 3: 'WED', 4: 'TH', 5: 'FR', 6: 'SA' }
  const forecast = [
    { day: 'Tuesday', icon: 'mdi-white-balance-sunny', temp: '24\u00B0/12\u00B0' },
    { day: 'Wednesday', icon: 'mdi-white-balance-sunny', temp: '22\u00B0/14\u00B0' },
    { day: 'Thursday', icon: 'mdi-cloud', temp: '25\u00B0/15\u00B0' },
  ]

  const expand = ref(false)
  const time = ref(0)
</script>

<script>
  export default {
    data: () => ({
      labels: { 0: 'SU', 1: 'MO', 2: 'TU', 3: 'WED', 4: 'TH', 5: 'FR', 6: 'SA' },
      expand: false,
      time: 0,
      forecast: [
        { day: 'Tuesday', icon: 'mdi-white-balance-sunny', temp: '24\xB0/12\xB0' },
        { day: 'Wednesday', icon: 'mdi-white-balance-sunny', temp: '22\xB0/14\xB0' },
        { day: 'Thursday', icon: 'mdi-cloud', temp: '25\xB0/15\xB0' },
      ],
    }),
  }
</script>

```

# Vuetify component v-card - prop color

Example code

```vue
<template>
  <v-row justify="center">
    <v-col cols="auto">
      <v-radio-group
        v-model="color"
        hide-details
        inline
      >
        <v-radio
          color="indigo"
          label="indigo"
          value="indigo"
        ></v-radio>

        <v-radio
          color="indigo-darken-3"
          label="indigo-darken-3"
          value="indigo-darken-3"
        ></v-radio>

        <v-radio
          color="primary"
          label="primary"
          value="primary"
        ></v-radio>

        <v-radio
          color="secondary"
          label="secondary"
          value="secondary"
        ></v-radio>
      </v-radio-group>
    </v-col>

    <v-col
      v-for="(variant, i) in variants"
      :key="i"
      cols="12"
      md="6"
    >
      <v-card
        :color="color"
        :variant="variant"
        class="mx-auto"
      >
        <v-card-item>
          <div>
            <div class="text-overline mb-1">
              {{ variant }}
            </div>
            <div class="text-h6 mb-1">
              Headline
            </div>
            <div class="text-caption">Greyhound divisely hello coldly fonwderfully</div>
          </div>
        </v-card-item>

        <v-card-actions>
          <v-btn>
            Button
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const variants = ['elevated', 'flat', 'tonal', 'outlined']
  const color = ref('indigo')
</script>

```

# Vuetify component v-card - basics content

Example code

```vue
<template>
  <v-row>
    <v-col cols="12" md="4">
      <v-card
        subtitle="This is a card subtitle"
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!"
        title="This is a title"
      ></v-card>

      <div class="text-center text-caption">Using Props Only</div>
    </v-col>

    <v-col cols="12" md="4">
      <v-card>
        <template v-slot:title>
          This is a title
        </template>

        <template v-slot:subtitle>
          This is a card subtitle
        </template>

        <template v-slot:text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!
        </template>
      </v-card>

      <div class="text-center text-caption">Using Slots Only</div>
    </v-col>

    <v-col cols="12" md="4">
      <v-card>
        <v-card-item>
          <v-card-title>This is a title</v-card-title>

          <v-card-subtitle>This is a card subtitle</v-card-subtitle>
        </v-card-item>

        <v-card-text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!
        </v-card-text>
      </v-card>

      <div class="text-center text-caption">Using Markup Only</div>
    </v-col>
  </v-row>
</template>

```

# Vuetify component v-card - slot prepend append

Example code

```vue
<template>
  <v-row align="center" justify="center" dense>
    <v-col cols="12" md="6">
      <v-card
        append-icon="mdi-check"
        class="mx-auto"
        prepend-icon="mdi-account"
        subtitle="prepend-icon and append-icon"
        title="Icons"
      >
        <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="12" md="6">
      <v-card
        class="mx-auto"
        subtitle="prepend and append"
        title="Icons"
      >
        <template v-slot:prepend>
          <v-icon color="primary" icon="mdi-account"></v-icon>
        </template>
        <template v-slot:append>
          <v-icon color="success" icon="mdi-check"></v-icon>
        </template>
        <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="12" md="6">
      <v-card
        append-avatar="https://cdn.vuetifyjs.com/images/john.jpg"
        class="mx-auto"
        prepend-avatar="https://cdn.vuetifyjs.com/images/logos/v-alt.svg"
        subtitle="prepend-avatar and append-avatar"
        title="Avatars"
      >
        <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="12" md="6">
      <v-card
        class="mx-auto"
        subtitle="prepend and append"
        title="Avatars"
      >
        <template v-slot:prepend>
          <v-avatar color="blue-darken-2">
            <v-icon icon="mdi-alarm"></v-icon>
          </v-avatar>
        </template>
        <template v-slot:append>
          <v-avatar size="24">
            <v-img
              alt="John"
              src="https://cdn.vuetifyjs.com/images/john.png"
            ></v-img>
          </v-avatar>
        </template>
        <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.</v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

```

# Vuetify component v-card - misc custom actions

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      cover
    ></v-img>

    <v-card-title>
      Top western road trips
    </v-card-title>

    <v-card-subtitle>
      1,000 miles of wonder
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange-lighten-2"
        text="Explore"
      ></v-btn>

      <v-spacer></v-spacer>

      <v-btn
        :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
        @click="show = !show"
      ></v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const show = ref(false)
</script>

<script>
  export default {
    data: () => ({
      show: false,
    }),
  }
</script>

```

# Vuetify component v-card - misc shopify funding

Example code

```vue
<template>
  <v-container>
    <v-card>
      <v-card-title class="text-overline">
        Progress

        <div class="text-green-darken-3 text-h3 font-weight-bold">90%</div>

        <div class="text-h6 text-medium-emphasis font-weight-regular">
          $2,938.00 remaining
        </div>
      </v-card-title>
      <br>
      <v-card-text>
        <div
          :style="`right: calc(${review} - 32px)`"
          class="position-absolute mt-n8 text-caption text-green-darken-3"
        >
          Eligibility review
        </div>
        <v-progress-linear
          color="green-darken-3"
          height="22"
          model-value="90"
          rounded="lg"
        >
          <v-badge
            :style="`right: ${review}`"
            class="position-absolute"
            color="white"
            dot
            inline
          ></v-badge>
        </v-progress-linear>

        <div class="d-flex justify-space-between py-3">
          <span class="text-green-darken-3 font-weight-medium">
            $26,442.00 remitted
          </span>

          <span class="text-medium-emphasis"> $29,380.00 total </span>
        </div>
      </v-card-text>

      <v-divider></v-divider>

      <v-list-item
        append-icon="mdi-chevron-right"
        lines="two"
        subtitle="Details and agreement"
        link
      ></v-list-item>
    </v-card>
  </v-container>
</template>

<script setup>
  const review = '30%'
</script>

<script>
  export default {
    data: () => ({ review: '30%' }),
  }
</script>

```

# Vuetify component v-card - prop href

Example code

```vue
<template>
  <v-card
    append-icon="mdi-open-in-new"
    class="mx-auto"
    href="https://github.com/vuetifyjs/vuetify/"
    max-width="344"
    prepend-icon="mdi-github"
    rel="noopener"
    subtitle="Check out the official repository"
    target="_blank"
    title="Vuetify on GitHub"
  ></v-card>
</template>

```

# Vuetify component v-card - basics combine

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    prepend-icon="$vuetify"
    subtitle="The #1 Vue UI Library"
    width="400"
  >
    <template v-slot:title>
      <span class="font-weight-black">Welcome to Vuetify</span>
    </template>

    <v-card-text class="bg-surface-light pt-4">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
    </v-card-text>
  </v-card>
</template>

```

# Vuetify component v-card - prop link

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
    subtitle="Same looks, no anchor"
    title="Hover and click me"
    link
  ></v-card>
</template>

```
