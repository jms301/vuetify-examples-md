# Vuetify component v-data-iterator - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
    :script="script"
  >
    <div>
      <v-data-iterator
        v-bind="props"
        :items="cards"
        :page="page"
        items-per-page="3"
      >
        <template v-slot:default="{ items }">
          <template
            v-for="(item, i) in items"
            :key="i"
          >
            <v-card v-bind="item.raw"></v-card>

            <br>
          </template>
        </template>

        <template v-slot:footer="{ pageCount }">
          <v-pagination v-model="page" :length="pageCount"></v-pagination>
        </template>
      </v-data-iterator>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-data-iterator'
  const model = ref('default')
  const options = []

  const page = ref(1)

  const cards = Array.from({ length: 15 }, (k, v) => ({
    title: `Item ${v + 1}`,
    text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!',
  }))

  const props = computed(() => {
    return {
      items: 'items',
      page: 'page',
    }
  })

  const slots = computed(() => {
    return `
  <template v-slot:default="{ items }">
    <template
      v-for="(item, i) in items"
      :key="i"
    >
      <v-card v-bind="item.raw"></v-card>

      <br>
    </template>
  </template>
`
  })

  const code = computed(() => {
    return `<v-data-iterator${propsToString(props.value, ['items'])}>${slots.value}</v-data-iterator>`
  })

  const script = computed(() => {
    return `<script setup>
  import { ref } from 'vue'

  const page = ref(1)
  const items = Array.from({ length: 15 }, (k, v) => ({
    title: 'Item ' + v + 1,
    text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!',
  }))
<` + '/script>'
  })
</script>

```

# Vuetify component v-data-iterator - misc filter

Example code

```vue
<template>
  <v-card>
    <v-data-iterator
      :items="games"
      :items-per-page="3"
      :search="search"
    >
      <template v-slot:header>
        <v-toolbar class="px-2">
          <v-text-field
            v-model="search"
            density="comfortable"
            placeholder="Search"
            prepend-inner-icon="mdi-magnify"
            style="max-width: 300px;"
            variant="solo"
            clearable
            hide-details
          ></v-text-field>
        </v-toolbar>
      </template>

      <template v-slot:default="{ items }">
        <v-container class="pa-2" fluid>
          <v-row dense>
            <v-col
              v-for="item in items"
              :key="item.title"
              cols="auto"
              md="4"
            >
              <v-card class="pb-3" border flat>
                <v-img :src="item.raw.img"></v-img>

                <v-list-item :subtitle="item.raw.subtitle" class="mb-2">
                  <template v-slot:title>
                    <strong class="text-h6 mb-2">{{ item.raw.title }}</strong>
                  </template>
                </v-list-item>

                <div class="d-flex justify-space-between px-4">
                  <div class="d-flex align-center text-caption text-medium-emphasis me-1">
                    <v-icon icon="mdi-clock" start></v-icon>

                    <div class="text-truncate">{{ item.raw.duration }}</div>
                  </div>

                  <v-btn
                    class="text-none"
                    size="small"
                    text="Read"
                    variant="flat"
                    border
                  >
                  </v-btn>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </template>

      <template v-slot:footer="{ page, pageCount, prevPage, nextPage }">
        <div class="d-flex align-center justify-center pa-4">
          <v-btn
            :disabled="page === 1"
            density="comfortable"
            icon="mdi-arrow-left"
            variant="tonal"
            rounded
            @click="prevPage"
          ></v-btn>

          <div class="mx-2 text-caption">
            Page {{ page }} of {{ pageCount }}
          </div>

          <v-btn
            :disabled="page >= pageCount"
            density="comfortable"
            icon="mdi-arrow-right"
            variant="tonal"
            rounded
            @click="nextPage"
          ></v-btn>
        </div>
      </template>
    </v-data-iterator>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const search = shallowRef('')
  const games = [
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/4.png',
      title: 'The Sci-Fi Shooter Experience',
      subtitle: 'Dive into a futuristic world of intense battles and alien encounters.',
      advanced: false,
      duration: '8 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/2.png',
      title: 'Epic Adventures in Open Worlds',
      subtitle: 'Embark on a journey through vast, immersive landscapes and quests.',
      advanced: true,
      duration: '10 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/3.png',
      title: 'Surviving the Space Station Horror',
      subtitle: 'Navigate a haunted space station in this chilling survival horror game.',
      advanced: false,
      duration: '9 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/5.png',
      title: 'Neon-Lit High-Speed Racing Thrills',
      subtitle: 'Experience adrenaline-pumping races in a futuristic, neon-soaked city.',
      advanced: true,
      duration: '12 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/6.png',
      title: 'Retro-Style Platformer Adventures',
      subtitle: 'Jump and dash through pixelated worlds in this classic-style platformer.',
      advanced: false,
      duration: '11 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/7.png',
      title: 'Medieval Strategic War Campaigns',
      subtitle: 'Lead armies into epic battles and conquer kingdoms in this strategic war game.',
      advanced: true,
      duration: '10 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/1.png',
      title: 'Underwater VR Exploration Adventure',
      subtitle: 'Dive deep into the ocean and discover the mysteries of the underwater world.',
      advanced: true,
      duration: '11 minutes',
    },
    {
      img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/8.png',
      title: '1920s Mystery Detective Chronicles',
      subtitle: 'Solve crimes and uncover secrets in the glamorous 1920s era.',
      advanced: false,
      duration: '9 minutes',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      search: '',
      games: [
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/4.png',
          title: 'The Sci-Fi Shooter Experience',
          subtitle: 'Dive into a futuristic world of intense battles and alien encounters.',
          advanced: false,
          duration: '8 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/2.png',
          title: 'Epic Adventures in Open Worlds',
          subtitle: 'Embark on a journey through vast, immersive landscapes and quests.',
          advanced: true,
          duration: '10 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/3.png',
          title: 'Surviving the Space Station Horror',
          subtitle: 'Navigate a haunted space station in this chilling survival horror game.',
          advanced: false,
          duration: '9 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/5.png',
          title: 'Neon-Lit High-Speed Racing Thrills',
          subtitle: 'Experience adrenaline-pumping races in a futuristic, neon-soaked city.',
          advanced: true,
          duration: '12 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/6.png',
          title: 'Retro-Style Platformer Adventures',
          subtitle: 'Jump and dash through pixelated worlds in this classic-style platformer.',
          advanced: false,
          duration: '11 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/7.png',
          title: 'Medieval Strategic War Campaigns',
          subtitle: 'Lead armies into epic battles and conquer kingdoms in this strategic game.',
          advanced: true,
          duration: '10 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/1.png',
          title: 'Underwater VR Exploration Adventure',
          subtitle: 'Dive deep into the ocean and discover the mysteries of the underwater world.',
          advanced: true,
          duration: '11 minutes',
        },
        {
          img: 'https://cdn.vuetifyjs.com/docs/images/graphics/games/8.png',
          title: '1920s Mystery Detective Chronicles',
          subtitle: 'Solve crimes and uncover secrets in the glamorous 1920s era.',
          advanced: false,
          duration: '9 minutes',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-iterator - slot header and footer

Example code

```vue
<template>
  <v-data-iterator
    :items="mice"
    :items-per-page="itemsPerPage"
  >
    <template v-slot:header="{ page, pageCount, prevPage, nextPage }">
      <h1 class="text-h4 font-weight-bold d-flex justify-space-between mb-4 align-center">
        <div class="text-truncate">
          Most popular mice
        </div>

        <div class="d-flex align-center">
          <v-btn
            class="me-8"
            variant="text"
            @click="onClickSeeAll"
          >
            <span class="text-decoration-underline text-none">See all</span>
          </v-btn>

          <div class="d-inline-flex">
            <v-btn
              :disabled="page === 1"
              class="me-2"
              icon="mdi-arrow-left"
              size="small"
              variant="tonal"
              @click="prevPage"
            ></v-btn>

            <v-btn
              :disabled="page === pageCount"
              icon="mdi-arrow-right"
              size="small"
              variant="tonal"
              @click="nextPage"
            ></v-btn>
          </div>
        </div>
      </h1>
    </template>

    <template v-slot:default="{ items }">
      <v-row>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
          sm="6"
          xl="3"
        >
          <v-sheet border>
            <v-img
              :gradient="`to top right, rgba(255, 255, 255, .1), rgba(${item.raw.color}, .15)`"
              :src="item.raw.src"
              height="150"
              cover
            ></v-img>

            <v-list-item
              :title="item.raw.name"
              density="comfortable"
              lines="two"
              subtitle="Lorem ipsum dil orei namdie dkaf"
            >
              <template v-slot:title>
                <strong class="text-h6">
                  {{ item.raw.name }}
                </strong>
              </template>
            </v-list-item>

            <v-table class="text-caption" density="compact">
              <tbody>
                <tr align="right">
                  <th>DPI:</th>

                  <td>{{ item.raw.dpi }}</td>
                </tr>

                <tr align="right">
                  <th>Buttons:</th>

                  <td>{{ item.raw.buttons }}</td>
                </tr>

                <tr align="right">
                  <th>Weight:</th>

                  <td>{{ item.raw.weight }}</td>
                </tr>

                <tr align="right">
                  <th>Wireless:</th>

                  <td>{{ item.raw.wireless ? 'Yes' : 'No' }}</td>
                </tr>

                <tr align="right">
                  <th>Price:</th>

                  <td>${{ item.raw.price }}</td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </v-col>
      </v-row>
    </template>

    <template v-slot:footer="{ page, pageCount }">
      <v-footer
        class="justify-space-between text-body-2 mt-4"
        color="surface-variant"
      >
        Total mice: {{ mice.length }}

        <div>
          Page {{ page }} of {{ pageCount }}
        </div>
      </v-footer>
    </template>
  </v-data-iterator>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const itemsPerPage = shallowRef(4)
  const mice = [
    {
      name: 'Logitech G Pro X',
      color: '14, 151, 210',
      dpi: 16000,
      buttons: 8,
      weight: '63g',
      wireless: true,
      price: 149.99,
      description: 'Logitech G Pro X',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/3.png',
    },
    {
      name: 'Razer DeathAdder V2',
      color: '12, 146, 47',
      dpi: 20000,
      buttons: 8,
      weight: '82g',
      wireless: false,
      price: 69.99,
      description: 'Razer DeathAdder V2',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/2.png',
    },
    {
      name: 'Corsair Dark Core RGB',
      color: '107, 187, 226',
      dpi: 18000,
      buttons: 9,
      weight: '133g',
      wireless: true,
      price: 89.99,
      description: 'Corsair Dark Core RGB',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/1.png',
    },
    {
      name: 'SteelSeries Rival 3',
      color: '228, 196, 69',
      dpi: 8500,
      buttons: 6,
      weight: '77g',
      wireless: false,
      price: 29.99,
      description: 'SteelSeries Rival 3',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/4.png',
    },
    {
      name: 'HyperX Pulsefire FPS Pro',
      color: '156, 82, 251',
      dpi: 16000,
      buttons: 6,
      weight: '95g',
      wireless: false,
      price: 44.99,
      description: 'HyperX Pulsefire FPS Pro',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/6.png',
    },
    {
      name: 'Zowie EC2',
      color: '166, 39, 222',
      dpi: 3200,
      buttons: 5,
      weight: '90g',
      wireless: false,
      price: 69.99,
      description: 'Zowie EC2',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/7.png',
    },
    {
      name: 'Roccat Kone AIMO',
      color: '131, 9, 10',
      dpi: 16000,
      buttons: 10,
      weight: '130g',
      wireless: false,
      price: 79.99,
      description: 'Roccat Kone AIMO',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/8.png',
    },
    {
      name: 'Logitech G903',
      color: '232, 94, 102',
      dpi: 12000,
      buttons: 11,
      weight: '110g',
      wireless: true,
      price: 129.99,
      description: 'Logitech G903',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/9.png',
    },
    {
      name: 'Cooler Master MM711',
      color: '58, 192, 239',
      dpi: 16000,
      buttons: 6,
      weight: '60g',
      wireless: false,
      price: 49.99,
      description: 'Cooler Master MM711',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/5.png',
    },
    {
      name: 'Glorious Model O',
      color: '161, 252, 250',
      dpi: 12000,
      buttons: 6,
      weight: '67g',
      wireless: false,
      price: 49.99,
      description: 'Glorious Model O',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/15.png',
    },
    {
      name: 'HP Omen Photon',
      color: '201, 1, 2',
      dpi: 16000,
      buttons: 11,
      weight: '128g',
      wireless: true,
      price: 99.99,
      description: 'HP Omen Photon',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/10.png',
    },
    {
      name: 'Asus ROG Chakram',
      color: '10, 181, 19',
      dpi: 16000,
      buttons: 9,
      weight: '121g',
      wireless: true,
      price: 159.99,
      description: 'Asus ROG Chakram',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/11.png',
    },
    {
      name: 'Razer Naga X',
      color: '100, 101, 102',
      dpi: 16000,
      buttons: 16,
      weight: '85g',
      wireless: false,
      price: 79.99,
      description: 'Razer Naga X',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/12.png',
    },
    {
      name: 'Mad Catz R.A.T. 8+',
      color: '136, 241, 242',
      dpi: 16000,
      buttons: 11,
      weight: '145g',
      wireless: false,
      price: 99.99,
      description: 'Mad Catz R.A.T. 8+',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/13.png',
    },
    {
      name: 'Alienware 610M',
      color: '109, 110, 114',
      dpi: 16000,
      buttons: 7,
      weight: '120g',
      wireless: true,
      price: 99.99,
      description: 'Alienware 610M',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/14.png',
    },
  ]

  function onClickSeeAll () {
    itemsPerPage.value = itemsPerPage.value === 4 ? mice.length : 4
  }
</script>

<script>
  export default {
    data () {
      return {
        itemsPerPage: 4,
        mice: [
          {
            name: 'Logitech G Pro X',
            color: '14, 151, 210',
            dpi: 16000,
            buttons: 8,
            weight: '63g',
            wireless: true,
            price: 149.99,
            description: 'Logitech G Pro X',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/3.png',
          },
          {
            name: 'Razer DeathAdder V2',
            color: '12, 146, 47',
            dpi: 20000,
            buttons: 8,
            weight: '82g',
            wireless: false,
            price: 69.99,
            description: 'Razer DeathAdder V2',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/2.png',
          },
          {
            name: 'Corsair Dark Core RGB',
            color: '107, 187, 226',
            dpi: 18000,
            buttons: 9,
            weight: '133g',
            wireless: true,
            price: 89.99,
            description: 'Corsair Dark Core RGB',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/1.png',
          },
          {
            name: 'SteelSeries Rival 3',
            color: '228, 196, 69',
            dpi: 8500,
            buttons: 6,
            weight: '77g',
            wireless: false,
            price: 29.99,
            description: 'SteelSeries Rival 3',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/4.png',
          },
          {
            name: 'HyperX Pulsefire FPS Pro',
            color: '156, 82, 251',
            dpi: 16000,
            buttons: 6,
            weight: '95g',
            wireless: false,
            price: 44.99,
            description: 'HyperX Pulsefire FPS Pro',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/6.png',
          },
          {
            name: 'Zowie EC2',
            color: '166, 39, 222',
            dpi: 3200,
            buttons: 5,
            weight: '90g',
            wireless: false,
            price: 69.99,
            description: 'Zowie EC2',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/7.png',
          },
          {
            name: 'Roccat Kone AIMO',
            color: '131, 9, 10',
            dpi: 16000,
            buttons: 10,
            weight: '130g',
            wireless: false,
            price: 79.99,
            description: 'Roccat Kone AIMO',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/8.png',
          },
          {
            name: 'Logitech G903',
            color: '232, 94, 102',
            dpi: 12000,
            buttons: 11,
            weight: '110g',
            wireless: true,
            price: 129.99,
            description: 'Logitech G903',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/9.png',
          },
          {
            name: 'Cooler Master MM711',
            color: '58, 192, 239',
            dpi: 16000,
            buttons: 6,
            weight: '60g',
            wireless: false,
            price: 49.99,
            description: 'Cooler Master MM711',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/5.png',
          },
          {
            name: 'Glorious Model O',
            color: '161, 252, 250',
            dpi: 12000,
            buttons: 6,
            weight: '67g',
            wireless: false,
            price: 49.99,
            description: 'Glorious Model O',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/15.png',
          },
          {
            name: 'HP Omen Photon',
            color: '201, 1, 2',
            dpi: 16000,
            buttons: 11,
            weight: '128g',
            wireless: true,
            price: 99.99,
            description: 'HP Omen Photon',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/10.png',
          },
          {
            name: 'Asus ROG Chakram',
            color: '10, 181, 19',
            dpi: 16000,
            buttons: 9,
            weight: '121g',
            wireless: true,
            price: 159.99,
            description: 'Asus ROG Chakram',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/11.png',
          },
          {
            name: 'Razer Naga X',
            color: '100, 101, 102',
            dpi: 16000,
            buttons: 16,
            weight: '85g',
            wireless: false,
            price: 79.99,
            description: 'Razer Naga X',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/12.png',
          },
          {
            name: 'Mad Catz R.A.T. 8+',
            color: '136, 241, 242',
            dpi: 16000,
            buttons: 11,
            weight: '145g',
            wireless: false,
            price: 99.99,
            description: 'Mad Catz R.A.T. 8+',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/13.png',
          },
          {
            name: 'Alienware 610M',
            color: '109, 110, 114',
            dpi: 16000,
            buttons: 7,
            weight: '120g',
            wireless: true,
            price: 99.99,
            description: 'Alienware 610M',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/14.png',
          },
        ],
      }
    },
    methods: {
      onClickSeeAll () {
        this.itemsPerPage = this.itemsPerPage === 4 ? this.mice.length : 4
      },
    },
  }
</script>

```

# Vuetify component v-data-iterator - slot loader

Example code

```vue
<template>
  <v-data-iterator
    :items="mice"
    :items-per-page="itemsPerPage"
    :loading="true"
  >
    <template v-slot:default="{ items }">
      <v-row>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
          sm="6"
          xl="3"
        >
          <v-sheet border>
            <v-img
              :gradient="`to top right, rgba(255, 255, 255, .1), rgba(${item.raw.color}, .15)`"
              :src="item.raw.src"
              height="150"
              cover
            ></v-img>

            <v-list-item
              :title="item.raw.name"
              density="comfortable"
              lines="two"
              subtitle="Lorem ipsum dil orei namdie dkaf"
            >
              <template v-slot:title>
                <strong class="text-h6">
                  {{ item.raw.name }}
                </strong>
              </template>
            </v-list-item>

            <v-table class="text-caption" density="compact">
              <tbody>
                <tr align="right">
                  <th>DPI:</th>

                  <td>{{ item.raw.dpi }}</td>
                </tr>

                <tr align="right">
                  <th>Buttons:</th>

                  <td>{{ item.raw.buttons }}</td>
                </tr>

                <tr align="right">
                  <th>Weight:</th>

                  <td>{{ item.raw.weight }}</td>
                </tr>

                <tr align="right">
                  <th>Wireless:</th>

                  <td>{{ item.raw.wireless ? 'Yes' : 'No' }}</td>
                </tr>

                <tr align="right">
                  <th>Price:</th>

                  <td>${{ item.raw.price }}</td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </v-col>
      </v-row>
    </template>

    <template v-slot:loader>
      <v-row>
        <v-col
          v-for="(_, k) in [0, 1, 2, 3]"
          :key="k"
          cols="12"
          sm="6"
          xl="3"
        >
          <v-skeleton-loader
            class="border"
            type="image, article"
          ></v-skeleton-loader>
        </v-col>
      </v-row>
    </template>

  </v-data-iterator>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const itemsPerPage = shallowRef(4)
  const mice = [
    {
      name: 'Logitech G Pro X',
      color: '14, 151, 210',
      dpi: 16000,
      buttons: 8,
      weight: '63g',
      wireless: true,
      price: 149.99,
      description: 'Logitech G Pro X',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/1.png',
    },
    {
      name: 'Razer DeathAdder V2',
      color: '12, 146, 47',
      dpi: 20000,
      buttons: 8,
      weight: '82g',
      wireless: false,
      price: 69.99,
      description: 'Razer DeathAdder V2',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/2.png',
    },
    {
      name: 'Corsair Dark Core RGB',
      color: '107, 187, 226',
      dpi: 18000,
      buttons: 9,
      weight: '133g',
      wireless: true,
      price: 89.99,
      description: 'Corsair Dark Core RGB',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/3.png',
    },
    {
      name: 'SteelSeries Rival 3',
      color: '228, 196, 69',
      dpi: 8500,
      buttons: 6,
      weight: '77g',
      wireless: false,
      price: 29.99,
      description: 'SteelSeries Rival 3',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/4.png',
    },
    {
      name: 'HyperX Pulsefire FPS Pro',
      color: '156, 82, 251',
      dpi: 16000,
      buttons: 6,
      weight: '95g',
      wireless: false,
      price: 44.99,
      description: 'HyperX Pulsefire FPS Pro',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/5.png',
    },
    {
      name: 'Zowie EC2',
      color: '166, 39, 222',
      dpi: 3200,
      buttons: 5,
      weight: '90g',
      wireless: false,
      price: 69.99,
      description: 'Zowie EC2',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/6.png',
    },
    {
      name: 'Roccat Kone AIMO',
      color: '131, 9, 10',
      dpi: 16000,
      buttons: 10,
      weight: '130g',
      wireless: false,
      price: 79.99,
      description: 'Roccat Kone AIMO',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/7.png',
    },
    {
      name: 'Logitech G903',
      color: '232, 94, 102',
      dpi: 12000,
      buttons: 11,
      weight: '110g',
      wireless: true,
      price: 129.99,
      description: 'Logitech G903',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/8.png',
    },
    {
      name: 'Cooler Master MM711',
      color: '58, 192, 239',
      dpi: 16000,
      buttons: 6,
      weight: '60g',
      wireless: false,
      price: 49.99,
      description: 'Cooler Master MM711',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/9.png',
    },
    {
      name: 'Glorious Model O',
      color: '161, 252, 250',
      dpi: 12000,
      buttons: 6,
      weight: '67g',
      wireless: false,
      price: 49.99,
      description: 'Glorious Model O',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/10.png',
    },
    {
      name: 'HP Omen Photon',
      color: '201, 1, 2',
      dpi: 16000,
      buttons: 11,
      weight: '128g',
      wireless: true,
      price: 99.99,
      description: 'HP Omen Photon',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/11.png',
    },
    {
      name: 'Asus ROG Chakram',
      color: '10, 181, 19',
      dpi: 16000,
      buttons: 9,
      weight: '121g',
      wireless: true,
      price: 159.99,
      description: 'Asus ROG Chakram',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/12.png',
    },
    {
      name: 'Razer Naga X',
      color: '100, 101, 102',
      dpi: 16000,
      buttons: 16,
      weight: '85g',
      wireless: false,
      price: 79.99,
      description: 'Razer Naga X',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/13.png',
    },
    {
      name: 'Mad Catz R.A.T. 8+',
      color: '136, 241, 242',
      dpi: 16000,
      buttons: 11,
      weight: '145g',
      wireless: false,
      price: 99.99,
      description: 'Mad Catz R.A.T. 8+',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/14.png',
    },
    {
      name: 'Alienware 610M',
      color: '109, 110, 114',
      dpi: 16000,
      buttons: 7,
      weight: '120g',
      wireless: true,
      price: 99.99,
      description: 'Alienware 610M',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/15.png',
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        itemsPerPage: 4,
        mice: [
          {
            name: 'Logitech G Pro X',
            color: '14, 151, 210',
            dpi: 16000,
            buttons: 8,
            weight: '63g',
            wireless: true,
            price: 149.99,
            description: 'Logitech G Pro X',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/1.png',
          },
          {
            name: 'Razer DeathAdder V2',
            color: '12, 146, 47',
            dpi: 20000,
            buttons: 8,
            weight: '82g',
            wireless: false,
            price: 69.99,
            description: 'Razer DeathAdder V2',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/2.png',
          },
          {
            name: 'Corsair Dark Core RGB',
            color: '107, 187, 226',
            dpi: 18000,
            buttons: 9,
            weight: '133g',
            wireless: true,
            price: 89.99,
            description: 'Corsair Dark Core RGB',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/3.png',
          },
          {
            name: 'SteelSeries Rival 3',
            color: '228, 196, 69',
            dpi: 8500,
            buttons: 6,
            weight: '77g',
            wireless: false,
            price: 29.99,
            description: 'SteelSeries Rival 3',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/4.png',
          },
          {
            name: 'HyperX Pulsefire FPS Pro',
            color: '156, 82, 251',
            dpi: 16000,
            buttons: 6,
            weight: '95g',
            wireless: false,
            price: 44.99,
            description: 'HyperX Pulsefire FPS Pro',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/5.png',
          },
          {
            name: 'Zowie EC2',
            color: '166, 39, 222',
            dpi: 3200,
            buttons: 5,
            weight: '90g',
            wireless: false,
            price: 69.99,
            description: 'Zowie EC2',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/6.png',
          },
          {
            name: 'Roccat Kone AIMO',
            color: '131, 9, 10',
            dpi: 16000,
            buttons: 10,
            weight: '130g',
            wireless: false,
            price: 79.99,
            description: 'Roccat Kone AIMO',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/7.png',
          },
          {
            name: 'Logitech G903',
            color: '232, 94, 102',
            dpi: 12000,
            buttons: 11,
            weight: '110g',
            wireless: true,
            price: 129.99,
            description: 'Logitech G903',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/8.png',
          },
          {
            name: 'Cooler Master MM711',
            color: '58, 192, 239',
            dpi: 16000,
            buttons: 6,
            weight: '60g',
            wireless: false,
            price: 49.99,
            description: 'Cooler Master MM711',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/9.png',
          },
          {
            name: 'Glorious Model O',
            color: '161, 252, 250',
            dpi: 12000,
            buttons: 6,
            weight: '67g',
            wireless: false,
            price: 49.99,
            description: 'Glorious Model O',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/10.png',
          },
          {
            name: 'HP Omen Photon',
            color: '201, 1, 2',
            dpi: 16000,
            buttons: 11,
            weight: '128g',
            wireless: true,
            price: 99.99,
            description: 'HP Omen Photon',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/11.png',
          },
          {
            name: 'Asus ROG Chakram',
            color: '10, 181, 19',
            dpi: 16000,
            buttons: 9,
            weight: '121g',
            wireless: true,
            price: 159.99,
            description: 'Asus ROG Chakram',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/12.png',
          },
          {
            name: 'Razer Naga X',
            color: '100, 101, 102',
            dpi: 16000,
            buttons: 16,
            weight: '85g',
            wireless: false,
            price: 79.99,
            description: 'Razer Naga X',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/13.png',
          },
          {
            name: 'Mad Catz R.A.T. 8+',
            color: '136, 241, 242',
            dpi: 16000,
            buttons: 11,
            weight: '145g',
            wireless: false,
            price: 99.99,
            description: 'Mad Catz R.A.T. 8+',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/14.png',
          },
          {
            name: 'Alienware 610M',
            color: '109, 110, 114',
            dpi: 16000,
            buttons: 7,
            weight: '120g',
            wireless: true,
            price: 99.99,
            description: 'Alienware 610M',
            src: 'https://cdn.vuetifyjs.com/docs/images/graphics/mice/15.png',
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-iterator - slot default

Example code

```vue
<template>
  <v-data-iterator
    :items="desserts"
    item-value="name"
  >
    <template v-slot:default="{ items, isExpanded, toggleExpand }">
      <v-row>
        <v-col
          v-for="item in items"
          :key="item.raw.name"
          cols="12"
          md="6"
          sm="12"
        >
          <v-card>
            <v-card-title class="d-flex align-center">
              <v-icon
                :color="item.raw.color"
                :icon="item.raw.icon"
                size="18"
                start
              ></v-icon>

              <h4>{{ item.raw.name }}</h4>
            </v-card-title>

            <v-card-text>
              {{ item.raw.description }}
            </v-card-text>

            <div class="px-4">
              <v-switch
                :label="`${isExpanded(item) ? 'Hide' : 'Show'} details`"
                :model-value="isExpanded(item)"
                density="compact"
                inset
                @click="() => toggleExpand(item)"
              ></v-switch>
            </div>

            <v-divider></v-divider>

            <v-expand-transition>
              <div v-if="isExpanded(item)">
                <v-list :lines="false" density="compact">
                  <v-list-item :title="`🔥 Calories: ${item.raw.calories}`" active></v-list-item>
                  <v-list-item :title="`🍔 Fat: ${item.raw.fat}`"></v-list-item>
                  <v-list-item :title="`🍞 Carbs: ${item.raw.carbs}`"></v-list-item>
                  <v-list-item :title="`🍗 Protein: ${item.raw.protein}`"></v-list-item>
                  <v-list-item :title="`🧂 Sodium: ${item.raw.sodium}`"></v-list-item>
                  <v-list-item :title="`🦴 Calcium: ${item.raw.calcium}`"></v-list-item>
                  <v-list-item :title="`🧲 Iron: ${item.raw.iron}`"></v-list-item>
                </v-list>
              </div>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </v-data-iterator>
</template>

<script setup>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      description: 'A tangy and creamy dessert made from yogurt and sometimes fruit, Frozen Yogurt is a lighter alternative to ice cream. Perfect for those who crave a sweet treat but want to keep it on the healthier side.',
      icon: 'mdi-ice-cream',
      color: '#6EC1E4',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      sodium: 87,
      calcium: '14%',
      iron: '1%',
    },
    {
      name: 'Ice cream sandwich',
      description: 'A classic treat featuring a layer of creamy ice cream sandwiched between two cookies or cake layers. Ideal for those hot summer days when you can\'t decide between a cookie and ice cream.',
      icon: 'mdi-cookie',
      color: '#F4A261',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      sodium: 129,
      calcium: '8%',
      iron: '1%',
    },
    {
      name: 'Eclair',
      description: 'A small, individual cake topped with frosting and often adorned with sprinkles or other decorations. Great for parties or as a quick indulgence when you need a sugar fix.',
      icon: 'mdi-cake-variant',
      color: '#6D4C41',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      sodium: 337,
      calcium: '6%',
      iron: '7%',
    },
    {
      name: 'Cupcake',
      description: 'A small, individual cake topped with frosting and often adorned with sprinkles or other decorations. Great for parties or as a quick indulgence when you need a sugar fix.',
      color: '#FFADAD',
      icon: 'mdi-cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      sodium: 413,
      calcium: '3%',
      iron: '8%',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      desserts: [
        {
          name: 'Frozen Yogurt',
          description: 'A tangy and creamy dessert made from yogurt and sometimes fruit, Frozen Yogurt is a lighter alternative to ice cream. Perfect for those who crave a sweet treat but want to keep it on the healthier side.',
          icon: 'mdi-ice-cream',
          color: '#6EC1E4',
          calories: 159,
          fat: 6,
          carbs: 24,
          protein: 4,
          sodium: 87,
          calcium: '14%',
          iron: '1%',
        },
        {
          name: 'Ice cream sandwich',
          description: 'A classic treat featuring a layer of creamy ice cream sandwiched between two cookies or cake layers. Ideal for those hot summer days when you can\'t decide between a cookie and ice cream.',
          icon: 'mdi-cookie',
          color: '#F4A261',
          calories: 237,
          fat: 9,
          carbs: 37,
          protein: 4.3,
          sodium: 129,
          calcium: '8%',
          iron: '1%',
        },
        {
          name: 'Eclair',
          description: 'A small, individual cake topped with frosting and often adorned with sprinkles or other decorations. Great for parties or as a quick indulgence when you need a sugar fix.',
          icon: 'mdi-cake-variant',
          color: '#6D4C41',
          calories: 262,
          fat: 16,
          carbs: 23,
          protein: 6,
          sodium: 337,
          calcium: '6%',
          iron: '7%',
        },
        {
          name: 'Cupcake',
          description: 'A small, individual cake topped with frosting and often adorned with sprinkles or other decorations. Great for parties or as a quick indulgence when you need a sugar fix.',
          color: '#FFADAD',
          icon: 'mdi-cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          sodium: 413,
          calcium: '3%',
          iron: '8%',
        },
      ],
    }),
  }
</script>

```
