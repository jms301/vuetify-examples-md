# Vuetify component v-hover - usage

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
      <v-hover v-bind="props">
        <template v-slot:default="{ isHovering, props: hoverProps }">
          <v-card
            v-bind="hoverProps"
            :color="isHovering ? 'primary' : undefined"
            text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
            title="Hover over me"
          ></v-card>
        </template>
      </v-hover>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-hover'
  const model = ref('default')
  const options = []
  const props = computed(() => {
    return {}
  })

  const slots = computed(() => {
    return `
  <template v-slot:default="{ isHovering, props }">
    <v-card
      v-bind="props"
      :color="isHovering ? 'primary' : undefined"
      title="Hover over me"
      text="..."
    ></v-card>
  </template>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-hover - misc hover list

Example code

```vue
<template>
  <v-container class="pa-4 text-center">
    <v-row
      align="center"
      class="fill-height"
      justify="center"
    >
      <template v-for="(item, i) in items" :key="i">
        <v-col
          cols="12"
          md="4"
        >
          <v-hover v-slot="{ isHovering, props }">
            <v-card
              :class="{ 'on-hover': isHovering }"
              :elevation="isHovering ? 12 : 2"
              v-bind="props"
            >
              <v-img
                :src="item.img"
                height="225px"
                cover
              >
                <v-card-title class="text-h6 text-white d-flex flex-column">
                  <p class="mt-4">
                    {{ item.title }}
                  </p>

                  <div>
                    <p class="ma-0 text-body-1 font-weight-bold">
                      {{ item.text }}
                    </p>
                    <p class="text-caption font-weight-medium">
                      {{ item.subtext }}
                    </p>
                  </div>
                </v-card-title>
                <div class="align-self-center">
                  <v-btn
                    v-for="(icon, index) in icons"
                    :key="index"
                    :class="{ 'show-btns': isHovering }"
                    :color="transparent"
                    :icon="icon"
                    variant="text"
                  ></v-btn>
                </div>
              </v-img>
            </v-card>
          </v-hover>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>

<script setup>
  const icons = ['mdi-rewind', 'mdi-play', 'mdi-fast-forward']
  const items = [
    {
      title: 'New Releases',
      text: `It's New Release Friday`,
      subtext: 'Newly released songs.',
      img: 'https://cdn.vuetifyjs.com/docs/images/cards/hands.jpg',
    },
    {
      title: 'Rock',
      text: 'Greatest Rock Hits',
      subtext: 'Lose yourself in rock tunes.',
      img: 'https://cdn.vuetifyjs.com/docs/images/cards/singer.jpg',
    },
    {
      title: 'Mellow Moods',
      text: 'Ambient Bass',
      subtext: 'Chill beats to mellow you out.',
      img: 'https://cdn.vuetifyjs.com/docs/images/cards/concert.jpg',
    },
  ]
  const transparent = 'rgba(255, 255, 255, 0)'
</script>

<script>
  export default {
    data: () => ({
      icons: ['mdi-rewind', 'mdi-play', 'mdi-fast-forward'],
      items: [
        {
          title: 'New Releases',
          text: `It's New Release Friday`,
          subtext: 'Newly released songs.',
          img: 'https://cdn.vuetifyjs.com/docs/images/cards/hands.jpg',
        },
        {
          title: 'Rock',
          text: 'Greatest Rock Hits',
          subtext: 'Lose yourself in rock tunes.',
          img: 'https://cdn.vuetifyjs.com/docs/images/cards/singer.jpg',
        },
        {
          title: 'Mellow Moods',
          text: 'Ambient Bass',
          subtext: 'Chill beats to mellow you out.',
          img: 'https://cdn.vuetifyjs.com/docs/images/cards/concert.jpg',
        },
      ],
      transparent: 'rgba(255, 255, 255, 0)',
    }),
  }
</script>

<style scoped>
  .v-card {
    transition: opacity .4s ease-in-out;
  }

  .v-card:not(.on-hover) {
    opacity: 0.6;
  }

  .show-btns {
    color: rgba(255, 255, 255, 1) !important;
  }
</style>

```

# Vuetify component v-hover - misc transition

Example code

```vue
<template>
  <div>
    <v-hover v-slot="{ isHovering, props }">
      <v-card
        class="mx-auto"
        color="grey-lighten-4"
        max-width="600"
        v-bind="props"
      >
        <v-img
          :aspect-ratio="16/9"
          src="https://cdn.vuetifyjs.com/images/cards/kitchen.png"
          cover
        >
          <v-expand-transition>
            <div
              v-if="isHovering"
              class="d-flex bg-orange-darken-2 v-card--reveal text-h2"
              style="height: 100%;"
            >
              $14.99
            </div>
          </v-expand-transition>
        </v-img>

        <v-card-text class="pt-6">
          <div class="font-weight-light text-grey text-h6 mb-2">
            For the perfect meal
          </div>

          <h3 class="text-h4 font-weight-light text-orange mb-2">
            QW cooking utensils
          </h3>

          <div class="font-weight-light text-h6 mb-2">
            Our Vintage kitchen utensils delight any chef.<br>
            Made of bamboo by hand
          </div>
        </v-card-text>
      </v-card>
    </v-hover>
  </div>
</template>

<style>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .9;
    position: absolute;
    width: 100%;
  }
</style>

```

# Vuetify component v-hover - prop disabled

Example code

```vue
<template>
  <v-row
    align="center"
    justify="center"
  >
    <v-col cols="12">
      <v-hover
        v-slot="{ isHovering, props }"
        disabled
      >
        <v-card
          :elevation="isHovering ? 12 : 2"
          class="mx-auto"
          height="350"
          max-width="350"
          v-bind="props"
        >
          <v-card-text class="my-4 text-center text-h6">
            Hover over me!
          </v-card-text>
        </v-card>
      </v-hover>
    </v-col>
  </v-row>
</template>

```

# Vuetify component v-hover - prop open and close delay

Example code

```vue
<template>
  <v-row>
    <v-col
      cols="12"
      sm="6"
    >
      <v-hover
        v-slot="{ isHovering, props }"
        open-delay="200"
      >
        <v-card
          :class="{ 'on-hover': isHovering }"
          :elevation="isHovering ? 16 : 2"
          class="mx-auto"
          height="350"
          max-width="350"
          v-bind="props"
        >
          <v-card-text class="font-weight-medium mt-12 text-center text-subtitle-1">
            Open Delay (Mouse enter)
          </v-card-text>
        </v-card>
      </v-hover>
    </v-col>

    <v-col
      cols="12"
      sm="6"
    >
      <v-hover
        v-slot="{ isHovering, props }"
        close-delay="200"
      >
        <v-card
          :class="{ 'on-hover': isHovering }"
          :elevation="isHovering ? 16 : 2"
          class="mx-auto"
          height="350"
          max-width="350"
          v-bind="props"
        >
          <v-card-text class="font-weight-medium mt-12 text-center text-subtitle-1">
            Close Delay (Mouse leave)
          </v-card-text>
        </v-card>
      </v-hover>
    </v-col>
  </v-row>
</template>

<style lang="sass" scoped>
.v-card.on-hover.v-theme--dark
  background-color: rgba(#FFF, 0.8)
  >.v-card__text
    color: #000
</style>

```
