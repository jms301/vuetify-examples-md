# Vuetify component v-data-table - usage

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
      <v-data-table
        v-bind="props"
        :items="items"
      ></v-data-table>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-data-table'
  const model = ref('default')
  const options = ['Hide header', 'Hide footer', 'Hide both']

  const items = [
    {
      name: 'African Elephant',
      species: 'Loxodonta africana',
      diet: 'Herbivore',
      habitat: 'Savanna, Forests',
    },
    {
      name: 'Lion',
      species: 'Panthera leo',
      diet: 'Carnivore',
      habitat: 'Savanna, Grassland',
    },
    {
      name: 'Giraffe',
      species: 'Giraffa camelopardalis',
      diet: 'Herbivore',
      habitat: 'Savanna, Grassland',
    },
    {
      name: 'Zebra',
      species: 'Equus quagga',
      diet: 'Herbivore',
      habitat: 'Savanna, Grassland',
    },
    {
      name: 'Hippopotamus',
      species: 'Hippopotamus amphibius',
      diet: 'Herbivore',
      habitat: 'Riverbanks, Lakes',
    },
    {
      name: 'Meerkat',
      species: 'Suricata suricatta',
      diet: 'Omnivore',
      habitat: 'Desert, Savanna',
    },
    {
      name: 'Hyena',
      species: 'Crocuta crocuta',
      diet: 'Carnivore',
      habitat: 'Savanna, Grassland',
    },
    {
      name: 'Zebra',
      species: 'Equus quagga',
      diet: 'Herbivore',
      habitat: 'Savanna, Grassland',
    },
    {
      name: 'Ostrich',
      species: 'Struthio camelus',
      diet: 'Omnivore',
      habitat: 'Savanna, Grassland',
    },
    {
      name: 'Cheetah',
      species: 'Acinonyx jubatus',
      diet: 'Carnivore',
      habitat: 'Savanna, Grassland',
    },
  ]

  const props = computed(() => {
    return {
      items: 'items',
      'hide-default-header': ['Hide both', 'Hide header'].includes(model.value) || undefined,
      'hide-default-footer': ['Hide both', 'Hide footer'].includes(model.value) || undefined,
    }
  })

  // eslint doesn't like the script tag inside the template
  const script = computed(() => {
    return `<script setup>
  const items = [
    {
      name: 'African Elephant',
      species: 'Loxodonta africana',
      diet: 'Herbivore',
      habitat: 'Savanna, Forests',
    },
    // ... more items
  ]
<` + '/script>'
  })

  const code = computed(() => {
    return `<v-data-table${propsToString(props.value, ['items'])}></v-data-table>`
  })
</script>

```

# Vuetify component v-data-table - prop sort by

Example code

```vue
<template>
  <v-data-table
    v-model:sort-by="sortBy"
    :headers="headers"
    :items="desserts"
  ></v-data-table>

  <pre>{{ sortBy }}</pre>
</template>

<script setup>
  import { ref } from 'vue'

  const sortBy = ref([{ key: 'calories', order: 'asc' }])

  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Calories', key: 'calories' },
    { title: 'Fat (g)', key: 'fat' },
    { title: 'Carbs (g)', key: 'carbs' },
    { title: 'Protein (g)', key: 'protein' },
    { title: 'Iron (%)', key: 'iron' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 200,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: '1%',
    },
    {
      name: 'Ice cream sandwich',
      calories: 200,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: '1%',
    },
    {
      name: 'Eclair',
      calories: 300,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: '7%',
    },
    {
      name: 'Cupcake',
      calories: 300,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8%',
    },
    {
      name: 'Gingerbread',
      calories: 400,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: '16%',
    },
    {
      name: 'Jelly bean',
      calories: 400,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: '0%',
    },
    {
      name: 'Lollipop',
      calories: 400,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2%',
    },
    {
      name: 'Honeycomb',
      calories: 400,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45%',
    },
    {
      name: 'Donut',
      calories: 500,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: '22%',
    },
    {
      name: 'KitKat',
      calories: 500,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: '6%',
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        sortBy: [{ key: 'calories', order: 'asc' }],
        headers: [
          {
            title: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            key: 'name',
          },
          { title: 'Calories', key: 'calories' },
          { title: 'Fat (g)', key: 'fat' },
          { title: 'Carbs (g)', key: 'carbs' },
          { title: 'Protein (g)', key: 'protein' },
          { title: 'Iron (%)', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 200,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Ice cream sandwich',
            calories: 200,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
          {
            name: 'Eclair',
            calories: 300,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Cupcake',
            calories: 300,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
          {
            name: 'Gingerbread',
            calories: 400,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%',
          },
          {
            name: 'Jelly bean',
            calories: 400,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%',
          },
          {
            name: 'Lollipop',
            calories: 400,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%',
          },
          {
            name: 'Honeycomb',
            calories: 400,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%',
          },
          {
            name: 'Donut',
            calories: 500,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%',
          },
          {
            name: 'KitKat',
            calories: 500,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%',
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - prop dense

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="plants"
    density="compact"
    item-key="name"
  ></v-data-table>
</template>

<script setup>
  const headers = [
    { title: 'Plant', align: 'start', sortable: false, key: 'name' },
    { title: 'Light', align: 'end', key: 'light' },
    { title: 'Height', align: 'end', key: 'height' },
    { title: 'Pet Friendly', align: 'end', key: 'petFriendly' },
    { title: 'Price ($)', align: 'end', key: 'price' },
  ]

  const plants = [
    {
      name: 'Fern',
      light: 'Low',
      height: '20cm',
      petFriendly: 'Yes',
      price: 20,
    },
    {
      name: 'Snake Plant',
      light: 'Low',
      height: '50cm',
      petFriendly: 'No',
      price: 35,
    },
    {
      name: 'Monstera',
      light: 'Medium',
      height: '60cm',
      petFriendly: 'No',
      price: 50,
    },
    {
      name: 'Pothos',
      light: 'Low to medium',
      height: '40cm',
      petFriendly: 'Yes',
      price: 25,
    },
    {
      name: 'ZZ Plant',
      light: 'Low to medium',
      height: '90cm',
      petFriendly: 'Yes',
      price: 30,
    },
    {
      name: 'Spider Plant',
      light: 'Bright, indirect',
      height: '30cm',
      petFriendly: 'Yes',
      price: 15,
    },
    {
      name: 'Air Plant',
      light: 'Bright, indirect',
      height: '15cm',
      petFriendly: 'Yes',
      price: 10,
    },
    {
      name: 'Peperomia',
      light: 'Bright, indirect',
      height: '25cm',
      petFriendly: 'Yes',
      price: 20,
    },
    {
      name: 'Aloe Vera',
      light: 'Bright, direct',
      height: '30cm',
      petFriendly: 'Yes',
      price: 15,
    },
    {
      name: 'Jade Plant',
      light: 'Bright, direct',
      height: '40cm',
      petFriendly: 'Yes',
      price: 25,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      headers: [
        { title: 'Plant', align: 'start', sortable: false, key: 'name' },
        { title: 'Light', align: 'end', key: 'light' },
        { title: 'Height', align: 'end', key: 'height' },
        { title: 'Pet Friendly', align: 'end', key: 'petFriendly' },
        { title: 'Price ($)', align: 'end', key: 'price' },
      ],
      plants: [
        {
          name: 'Fern',
          light: 'Low',
          height: '20cm',
          petFriendly: 'Yes',
          price: 20,
        },
        {
          name: 'Snake Plant',
          light: 'Low',
          height: '50cm',
          petFriendly: 'No',
          price: 35,
        },
        {
          name: 'Monstera',
          light: 'Medium',
          height: '60cm',
          petFriendly: 'No',
          price: 50,
        },
        {
          name: 'Pothos',
          light: 'Low to medium',
          height: '40cm',
          petFriendly: 'Yes',
          price: 25,
        },
        {
          name: 'ZZ Plant',
          light: 'Low to medium',
          height: '90cm',
          petFriendly: 'Yes',
          price: 30,
        },
        {
          name: 'Spider Plant',
          light: 'Bright, indirect',
          height: '30cm',
          petFriendly: 'Yes',
          price: 15,
        },
        {
          name: 'Air Plant',
          light: 'Bright, indirect',
          height: '15cm',
          petFriendly: 'Yes',
          price: 10,
        },
        {
          name: 'Peperomia',
          light: 'Bright, indirect',
          height: '25cm',
          petFriendly: 'Yes',
          price: 20,
        },
        {
          name: 'Aloe Vera',
          light: 'Bright, direct',
          height: '30cm',
          petFriendly: 'Yes',
          price: 15,
        },
        {
          name: 'Jade Plant',
          light: 'Bright, direct',
          height: '40cm',
          petFriendly: 'Yes',
          price: 25,
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - slot loading

Example code

```vue
<template>
  <div class="text-center mt-2 mb-4">
    <v-btn
      :disabled="loading"
      prepend-icon="mdi-refresh"
      rounded="lg"
      text="Refresh"
      variant="text"
      border
      @click="onClick"
    ></v-btn>
  </div>

  <v-sheet border rounded>
    <v-data-table :items="items" :loading="loading">
      <template v-slot:loading>
        <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
      </template>

      <template v-slot:item.horsepower="{ value }">
        <div class="text-medium-emphasis">
          <span>{{ value }}</span>

          <v-icon icon="mdi-horse-variant-fast" end></v-icon>
        </div>
      </template>

      <template v-slot:item.torque="{ value }">
        <div class="text-medium-emphasis">
          <span>{{ value }}</span>

          <v-icon icon="mdi-tire" end></v-icon>
        </div>
      </template>
    </v-data-table>
  </v-sheet>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const loading = shallowRef(false)

  const items = [
    { name: 'Chevrolet Camaro', year: 1967, engine: 'V8', horsepower: 375, torque: 415 },
    { name: 'Ford Mustang', year: 1965, engine: 'V8', horsepower: 271, torque: 312 },
    { name: 'Dodge Charger', year: 1968, engine: 'V8', horsepower: 425, torque: 490 },
    { name: 'Pontiac GTO', year: 1964, engine: 'V8', horsepower: 350, torque: 445 },
    { name: 'Plymouth Barracuda', year: 1964, engine: 'V8', horsepower: 330, torque: 425 },
    { name: 'Chevrolet Chevelle SS', year: 1970, engine: 'V8', horsepower: 450, torque: 500 },
    { name: 'Oldsmobile 442', year: 1971, engine: 'V8', horsepower: 340, torque: 440 },
    { name: 'Dodge Challenger', year: 1970, engine: 'V8', horsepower: 425, torque: 490 },
    { name: 'AMC Javelin', year: 1968, engine: 'V8', horsepower: 315, torque: 425 },
    { name: 'Mercury Cougar', year: 1967, engine: 'V8', horsepower: 335, torque: 427 },
  ]

  function onClick () {
    loading.value = true
    setTimeout(() => {
      loading.value = false
    }, 2000)
  }
</script>

<script>
  import { shallowRef } from 'vue'

  export default {
    data () {
      return {
        loading: false,
        items: [
          { name: 'Chevrolet Camaro', year: 1967, engine: 'V8', horsepower: 375, torque: 415 },
          { name: 'Ford Mustang', year: 1965, engine: 'V8', horsepower: 271, torque: 312 },
          { name: 'Dodge Charger', year: 1968, engine: 'V8', horsepower: 425, torque: 490 },
          { name: 'Pontiac GTO', year: 1964, engine: 'V8', horsepower: 350, torque: 445 },
          { name: 'Plymouth Barracuda', year: 1964, engine: 'V8', horsepower: 330, torque: 425 },
          { name: 'Chevrolet Chevelle SS', year: 1970, engine: 'V8', horsepower: 450, torque: 500 },
          { name: 'Oldsmobile 442', year: 1971, engine: 'V8', horsepower: 340, torque: 440 },
          { name: 'Dodge Challenger', year: 1970, engine: 'V8', horsepower: 425, torque: 490 },
          { name: 'AMC Javelin', year: 1968, engine: 'V8', horsepower: 315, torque: 425 },
          { name: 'Mercury Cougar', year: 1967, engine: 'V8', horsepower: 335, torque: 427 },
        ],
      }
    },
    methods: {
      onClick () {
        this.loading = true
        setTimeout(() => {
          this.loading = false
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop filter keys

Example code

```vue
<template>
  <v-card flat>
    <v-card-title class="d-flex align-center pe-2">
      <v-icon icon="mdi-video-input-component"></v-icon> &nbsp;
      Find a Graphics Card

      <v-spacer></v-spacer>

      <v-text-field
        v-model="search"
        density="compact"
        label="Search"
        prepend-inner-icon="mdi-magnify"
        variant="solo-filled"
        flat
        hide-details
        single-line
      ></v-text-field>
    </v-card-title>

    <v-divider></v-divider>
    <v-data-table
      v-model:search="search"
      :filter-keys="['name']"
      :items="items"
    >
      <template v-slot:header.stock>
        <div class="text-end">Stock</div>
      </template>

      <template v-slot:item.image="{ item }">
        <v-card class="my-2" elevation="2" rounded>
          <v-img
            :src="`https://cdn.vuetifyjs.com/docs/images/graphics/gpus/${item.image}`"
            height="64"
            cover
          ></v-img>
        </v-card>
      </template>

      <template v-slot:item.rating="{ item }">
        <v-rating
          :model-value="item.rating"
          color="orange-darken-2"
          density="compact"
          size="small"
          readonly
        ></v-rating>
      </template>

      <template v-slot:item.stock="{ item }">
        <div class="text-end">
          <v-chip
            :color="item.stock ? 'green' : 'red'"
            :text="item.stock ? 'In stock' : 'Out of stock'"
            class="text-uppercase"
            size="small"
            label
          ></v-chip>
        </div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const search = ref('')
  const items = [
    {
      name: 'Nebula GTX 3080',
      image: '1.png',
      price: 699.99,
      rating: 5,
      stock: true,
    },
    {
      name: 'Galaxy RTX 3080',
      image: '2.png',
      price: 799.99,
      rating: 4,
      stock: false,
    },
    {
      name: 'Orion RX 6800 XT',
      image: '3.png',
      price: 649.99,
      rating: 3,
      stock: true,
    },
    {
      name: 'Vortex RTX 3090',
      image: '4.png',
      price: 1499.99,
      rating: 4,
      stock: true,
    },
    {
      name: 'Cosmos GTX 1660 Super',
      image: '5.png',
      price: 299.99,
      rating: 4,
      stock: false,
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        search: '',
        items: [
          {
            name: 'Nebula GTX 3080',
            image: '1.png',
            price: 699.99,
            rating: 5,
            stock: true,
          },
          {
            name: 'Galaxy RTX 3080',
            image: '2.png',
            price: 799.99,
            rating: 4,
            stock: false,
          },
          {
            name: 'Orion RX 6800 XT',
            image: '3.png',
            price: 649.99,
            rating: 3,
            stock: true,
          },
          {
            name: 'Vortex RTX 3090',
            image: '4.png',
            price: 1499.99,
            rating: 4,
            stock: true,
          },
          {
            name: 'Cosmos GTX 1660 Super',
            image: '5.png',
            price: 299.99,
            rating: 4,
            stock: false,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - headers multiple

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="items"
    item-key="name"
    hide-default-footer
  ></v-data-table>
</template>

<script setup>
  const headers = [
    { title: 'Pyramid', value: 'name' },
    { title: 'Location', value: 'location' },
    { title: 'Construction Date', value: 'constructionDate' },
    {
      title: 'Dimensions',
      align: 'center',
      children: [
        { title: 'Height(m)', value: 'height' },
        { title: 'Base(m)', value: 'base' },
        { title: 'Volume(m³)', value: 'volume' },
      ],
    },
  ]

  const items = [
    {
      name: 'Great Pyramid of Giza',
      location: 'Egypt',
      height: '146.6',
      base: '230.4',
      volume: '2583285',
      constructionDate: 'c. 2580–2560 BC',
    },
    {
      name: 'Pyramid of Khafre',
      location: 'Egypt',
      height: '136.4',
      base: '215.3',
      volume: '1477485',
      constructionDate: 'c. 2570 BC',
    },
    {
      name: 'Red Pyramid',
      location: 'Egypt',
      height: '104',
      base: '220',
      volume: '1602895',
      constructionDate: 'c. 2590 BC',
    },
    {
      name: 'Bent Pyramid',
      location: 'Egypt',
      height: '101.1',
      base: '188.6',
      volume: '1200690',
      constructionDate: 'c. 2600 BC',
    },
    {
      name: 'Pyramid of the Sun',
      location: 'Mexico',
      height: '65',
      base: '225',
      volume: '1237097',
      constructionDate: 'c. 200 CE',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      headers: [
        { title: 'Pyramid', value: 'name' },
        { title: 'Location', value: 'location' },
        { title: 'Construction Date', value: 'constructionDate' },
        {
          title: 'Dimensions',
          align: 'center',
          children: [
            { title: 'Height(m)', value: 'height' },
            { title: 'Base(m)', value: 'base' },
            { title: 'Volume(m³)', value: 'volume' },
          ],
        },
      ],
      items: [
        {
          name: 'Great Pyramid of Giza',
          location: 'Egypt',
          height: '146.6',
          base: '230.4',
          volume: '2583285',
          constructionDate: 'c. 2580–2560 BC',
        },
        {
          name: 'Pyramid of Khafre',
          location: 'Egypt',
          height: '136.4',
          base: '215.3',
          volume: '1477485',
          constructionDate: 'c. 2570 BC',
        },
        {
          name: 'Red Pyramid',
          location: 'Egypt',
          height: '104',
          base: '220',
          volume: '1602895',
          constructionDate: 'c. 2590 BC',
        },
        {
          name: 'Bent Pyramid',
          location: 'Egypt',
          height: '101.1',
          base: '188.6',
          volume: '1200690',
          constructionDate: 'c. 2600 BC',
        },
        {
          name: 'Pyramid of the Sun',
          location: 'Mexico',
          height: '65',
          base: '225',
          volume: '1237097',
          constructionDate: 'c. 200 CE',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - prop search

Example code

```vue
<template>
  <v-card
    title="Nutrition"
    flat
  >
    <template v-slot:text>
      <v-text-field
        v-model="search"
        label="Search"
        prepend-inner-icon="mdi-magnify"
        variant="outlined"
        hide-details
        single-line
      ></v-text-field>
    </template>

    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const search = ref('')
  const headers = [
    {
      align: 'start',
      key: 'name',
      sortable: false,
      title: 'Dessert (100g serving)',
    },
    { key: 'calories', title: 'Calories' },
    { key: 'fat', title: 'Fat (g)' },
    { key: 'carbs', title: 'Carbs (g)' },
    { key: 'protein', title: 'Protein (g)' },
    { key: 'iron', title: 'Iron (%)' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            align: 'start',
            key: 'name',
            sortable: false,
            title: 'Dessert (100g serving)',
          },
          { key: 'calories', title: 'Calories' },
          { key: 'fat', title: 'Fat (g)' },
          { key: 'carbs', title: 'Carbs (g)' },
          { key: 'protein', title: 'Protein (g)' },
          { key: 'iron', title: 'Iron (%)' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - slot headers

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    item-value="name"
    items-per-page="5"
    hover
  >
    <template v-slot:top>
      <v-expand-transition>
        <div v-if="headers.length < 6">
          <v-btn
            class="mb-2"
            rounded="lg"
            size="small"
            text="Reset"
            variant="text"
            block
            border
            @click="onClickReset"
          ></v-btn>

          <v-divider></v-divider>
        </div>
      </v-expand-transition>
    </template>

    <template v-slot:headers="{ columns, isSorted, getSortIcon, toggleSort }">
      <tr>
        <template v-for="column in columns" :key="column.key">
          <th>
            <div class="d-flex align-center">
              <span
                class="me-2 cursor-pointer"
                @click="toggleSort(column)"
                v-text="column.title"
              ></span>

              <v-icon
                v-if="isSorted(column)"
                :icon="getSortIcon(column)"
                color="medium-emphasis"
              ></v-icon>

              <v-icon
                v-if="column.removable"
                color="medium-emphasis"
                icon="$close"
                @click="remove(column.key)"
              ></v-icon>
            </div>
          </th>
        </template>
      </tr>
    </template>
  </v-data-table>
</template>

<script setup>
  import { ref } from 'vue'

  function DEFAULT_HEADERS () {
    return [
      {
        title: 'Dessert',
        align: 'start',
        key: 'name',
        sortable: false,
        removable: false,
      },
      { title: 'Calories', key: 'calories', removable: true },
      { title: 'Fat(g)', key: 'fat', removable: true },
      { title: 'Carbs(g)', key: 'carbs', removable: true },
      { title: 'Protein(g)', key: 'protein', removable: true },
      { title: 'Iron(%)', key: 'iron', removable: true },
    ]
  }

  const headers = ref(DEFAULT_HEADERS())

  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]

  function onClickReset () {
    headers.value = DEFAULT_HEADERS()
  }

  function remove (key) {
    headers.value = headers.value.filter(header => header.key !== key)
  }
</script>

<script>
  function DEFAULT_HEADERS () {
    return [
      {
        title: 'Dessert',
        align: 'start',
        key: 'name',
        sortable: false,
        removable: false,
      },
      { title: 'Calories', key: 'calories', removable: true },
      { title: 'Fat(g)', key: 'fat', removable: true },
      { title: 'Carbs(g)', key: 'carbs', removable: true },
      { title: 'Protein(g)', key: 'protein', removable: true },
      { title: 'Iron(%)', key: 'iron', removable: true },
    ]
  }

  export default {
    data: () => ({
      headers: DEFAULT_HEADERS(),
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: 1,
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: 1,
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: 7,
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: 8,
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: 16,
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: 0,
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: 2,
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: 45,
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: 22,
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: 6,
        },
      ],
    }),
    methods: {
      onClickReset () {
        this.headers = DEFAULT_HEADERS()
      },
      remove (key) {
        this.headers = this.headers.filter(header => header.key !== key)
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop loading

Example code

```vue
<template>
  <v-data-table-server
    :items-length="0"
    item-key="name"
    loading-text="Loading... Please wait"
    loading
  ></v-data-table-server>
</template>

```

# Vuetify component v-data-table - misc crud

Example code

```vue
<template>
  <v-sheet border rounded>
    <v-data-table
      :headers="headers"
      :hide-default-footer="books.length < 11"
      :items="books"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>
            <v-icon color="medium-emphasis" icon="mdi-book-multiple" size="x-small" start></v-icon>

            Popular books
          </v-toolbar-title>

          <v-btn
            class="me-2"
            prepend-icon="mdi-plus"
            rounded="lg"
            text="Add a Book"
            border
            @click="add"
          ></v-btn>
        </v-toolbar>
      </template>

      <template v-slot:item.title="{ value }">
        <v-chip :text="value" border="thin opacity-25" prepend-icon="mdi-book" label>
          <template v-slot:prepend>
            <v-icon color="medium-emphasis"></v-icon>
          </template>
        </v-chip>
      </template>

      <template v-slot:item.actions="{ item }">
        <div class="d-flex ga-2 justify-end">
          <v-icon color="medium-emphasis" icon="mdi-pencil" size="small" @click="edit(item.id)"></v-icon>

          <v-icon color="medium-emphasis" icon="mdi-delete" size="small" @click="remove(item.id)"></v-icon>
        </div>
      </template>

      <template v-slot:no-data>
        <v-btn
          prepend-icon="mdi-backup-restore"
          rounded="lg"
          text="Reset data"
          variant="text"
          border
          @click="reset"
        ></v-btn>
      </template>
    </v-data-table>
  </v-sheet>

  <v-dialog v-model="dialog" max-width="500">
    <v-card
      :subtitle="`${isEditing ? 'Update' : 'Create'} your favorite book`"
      :title="`${isEditing ? 'Edit' : 'Add'} a Book`"
    >
      <template v-slot:text>
        <v-row>
          <v-col cols="12">
            <v-text-field v-model="record.title" label="Title"></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field v-model="record.author" label="Author"></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-select v-model="record.genre" :items="['Fiction', 'Dystopian', 'Non-Fiction', 'Sci-Fi']" label="Genre"></v-select>
          </v-col>

          <v-col cols="12" md="6">
            <v-number-input v-model="record.year" :max="adapter.getYear(adapter.date())" :min="1" label="Year"></v-number-input>
          </v-col>

          <v-col cols="12" md="6">
            <v-number-input v-model="record.pages" :min="1" label="Pages"></v-number-input>
          </v-col>
        </v-row>
      </template>

      <v-divider></v-divider>

      <v-card-actions class="bg-surface-light">
        <v-btn text="Cancel" variant="plain" @click="dialog = false"></v-btn>

        <v-spacer></v-spacer>

        <v-btn text="Save" @click="save"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
  import { onMounted, ref, shallowRef } from 'vue'
  import { useDate } from 'vuetify'

  const adapter = useDate()

  const DEFAULT_RECORD = { title: '', author: '', genre: '', year: adapter.getYear(adapter.date()), pages: 1 }

  const books = ref([])
  const record = ref(DEFAULT_RECORD)
  const dialog = shallowRef(false)
  const isEditing = shallowRef(false)

  const headers = [
    { title: 'Title', key: 'title', align: 'start' },
    { title: 'Author', key: 'author' },
    { title: 'Genre', key: 'genre' },
    { title: 'Year', key: 'year', align: 'end' },
    { title: 'Pages', key: 'pages', align: 'end' },
    { title: 'Actions', key: 'actions', align: 'end', sortable: false },
  ]

  onMounted(() => {
    reset()
  })

  function add () {
    isEditing.value = false
    record.value = DEFAULT_RECORD
    dialog.value = true
  }

  function edit (id) {
    isEditing.value = true

    const found = books.value.find(book => book.id === id)

    record.value = {
      id: found.id,
      title: found.title,
      author: found.author,
      genre: found.genre,
      year: found.year,
      pages: found.pages,
    }

    dialog.value = true
  }

  function remove (id) {
    const index = books.value.findIndex(book => book.id === id)
    books.value.splice(index, 1)
  }

  function save () {
    if (isEditing.value) {
      const index = books.value.findIndex(book => book.id === record.value.id)
      books.value[index] = record.value
    } else {
      record.value.id = books.value.length + 1
      books.value.push(record.value)
    }

    dialog.value = false
  }

  function reset () {
    dialog.value = false
    record.value = DEFAULT_RECORD
    books.value = [
      { id: 1, title: 'To Kill a Mockingbird', author: 'Harper Lee', genre: 'Fiction', year: 1960, pages: 281 },
      { id: 2, title: '1984', author: 'George Orwell', genre: 'Dystopian', year: 1949, pages: 328 },
      { id: 3, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', genre: 'Fiction', year: 1925, pages: 180 },
      { id: 4, title: 'Sapiens', author: 'Yuval Noah Harari', genre: 'Non-Fiction', year: 2011, pages: 443 },
      { id: 5, title: 'Dune', author: 'Frank Herbert', genre: 'Sci-Fi', year: 1965, pages: 412 },
    ]
  }
</script>

<script>
  import { onMounted, ref, shallowRef } from 'vue'
  import { useDate } from 'vuetify'

  export default {
    data () {
      const adapter = useDate()
      return {
        adapter,
        DEFAULT_RECORD: { title: '', author: '', genre: '', year: adapter.getYear(adapter.date()), pages: 1 },
        books: [],
        record: { title: '', author: '', genre: '', year: adapter.getYear(adapter.date()), pages: 1 },
        dialog: false,
        isEditing: false,
        headers: [
          { title: 'Title', key: 'title', align: 'start' },
          { title: 'Author', key: 'author' },
          { title: 'Genre', key: 'genre' },
          { title: 'Year', key: 'year', align: 'end' },
          { title: 'Pages', key: 'pages', align: 'end' },
          { title: 'Actions', key: 'actions', align: 'end', sortable: false },
        ],
      }
    },
    mounted () {
      this.reset()
    },
    methods: {
      add () {
        this.isEditing = false
        this.record = { ...this.DEFAULT_RECORD }
        this.dialog = true
      },
      edit (id) {
        this.isEditing = true
        const found = this.books.find(book => book.id === id)
        this.record = { ...found }
        this.dialog = true
      },
      remove (id) {
        const index = this.books.findIndex(book => book.id === id)
        this.books.splice(index, 1)
      },
      save () {
        if (this.isEditing) {
          const index = this.books.findIndex(book => book.id === this.record.id)
          this.books[index] = { ...this.record }
        } else {
          this.record.id = this.books.length + 1
          this.books.push({ ...this.record })
        }
        this.dialog = false
      },
      reset () {
        this.dialog = false
        this.record = { ...this.DEFAULT_RECORD }
        this.books = [
          { id: 1, title: 'To Kill a Mockingbird', author: 'Harper Lee', genre: 'Fiction', year: 1960, pages: 281 },
          { id: 2, title: '1984', author: 'George Orwell', genre: 'Dystopian', year: 1949, pages: 328 },
          { id: 3, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', genre: 'Fiction', year: 1925, pages: 180 },
          { id: 4, title: 'Sapiens', author: 'Yuval Noah Harari', genre: 'Non-Fiction', year: 2011, pages: 443 },
          { id: 5, title: 'Dune', author: 'Frank Herbert', genre: 'Sci-Fi', year: 1965, pages: 412 },
        ]
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop hide header footer

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    hide-default-footer
    hide-default-header
  ></v-data-table>
</template>

<script setup>
  const headers = [
    {
      title: 'Dessert(100g serving)',
      align: 'start',
      key: 'name',
    },
    { title: 'Calories', align: 'end', key: 'calories' },
    { title: 'Fat(g)', align: 'end', key: 'fat' },
    { title: 'Carbs(g)', align: 'end', key: 'carbs' },
    { title: 'Protein(g)', align: 'end', key: 'protein' },
    { title: 'Iron(%)', align: 'end', key: 'iron' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: '1%',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: '1%',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: '7%',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8%',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: '16%',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: '0%',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2%',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45%',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: '22%',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: '6%',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      headers: [
        {
          title: 'Dessert(100g serving)',
          align: 'start',
          key: 'name',
        },
        { title: 'Calories', align: 'end', key: 'calories' },
        { title: 'Fat(g)', align: 'end', key: 'fat' },
        { title: 'Carbs(g)', align: 'end', key: 'carbs' },
        { title: 'Protein(g)', align: 'end', key: 'protein' },
        { title: 'Iron(%)', align: 'end', key: 'iron' },
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: '1%',
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: '1%',
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: '7%',
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: '8%',
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: '16%',
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: '0%',
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: '2%',
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: '45%',
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: '22%',
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: '6%',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - misc server side paginate and sort

Example code

```vue
<template>
  <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    :items-length="totalItems"
    :loading="loading"
    :search="search"
    item-value="name"
    @update:options="loadItems"
  ></v-data-table-server>
</template>

<script setup>
  import { ref } from 'vue'

  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: '1',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: '0',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: '6',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: '7',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: '16',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: '1',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: '22',
    },
  ]
  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice()
          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }
          const paginated = items.slice(start, end === -1 ? undefined : end)
          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Calories', key: 'calories', align: 'end' },
    { title: 'Fat (g)', key: 'fat', align: 'end' },
    { title: 'Carbs (g)', key: 'carbs', align: 'end' },
    { title: 'Protein (g)', key: 'protein', align: 'end' },
    { title: 'Iron (%)', key: 'iron', align: 'end' },
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
    FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
      serverItems.value = items
      totalItems.value = total
      loading.value = false
    })
  }
</script>

<script>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6.0,
      carbs: 24,
      protein: 4.0,
      iron: '1',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0.0,
      carbs: 94,
      protein: 0.0,
      iron: '0',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26.0,
      carbs: 65,
      protein: 7,
      iron: '6',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16.0,
      carbs: 23,
      protein: 6.0,
      iron: '7',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16.0,
      carbs: 49,
      protein: 3.9,
      iron: '16',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9.0,
      carbs: 37,
      protein: 4.3,
      iron: '1',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25.0,
      carbs: 51,
      protein: 4.9,
      iron: '22',
    },
  ]

  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice()

          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }

          const paginated = items.slice(start, end)

          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }

  export default {
    data: () => ({
      itemsPerPage: 5,
      headers: [
        {
          title: 'Dessert (100g serving)',
          align: 'start',
          sortable: false,
          key: 'name',
        },
        { title: 'Calories', key: 'calories', align: 'end' },
        { title: 'Fat (g)', key: 'fat', align: 'end' },
        { title: 'Carbs (g)', key: 'carbs', align: 'end' },
        { title: 'Protein (g)', key: 'protein', align: 'end' },
        { title: 'Iron (%)', key: 'iron', align: 'end' },
      ],
      search: '',
      serverItems: [],
      loading: true,
      totalItems: 0,
    }),
    methods: {
      loadItems ({ page, itemsPerPage, sortBy }) {
        this.loading = true
        FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
          this.serverItems = items
          this.totalItems = total
          this.loading = false
        })
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop return object

Example code

```vue
<template>
  <v-data-table
    v-model="selected"
    :headers="headers"
    :items="desserts"
    item-value="name"
    items-per-page="5"
    return-object
    show-select
  ></v-data-table>

  <pre>{{ selected }}</pre>
</template>

<script setup>
  import { ref } from 'vue'

  const selected = ref([])

  const headers = ref([
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      key: 'name',
    },
    { title: 'Calories', align: 'end', key: 'calories' },
    { title: 'Fat (g)', align: 'end', key: 'fat' },
    { title: 'Carbs (g)', align: 'end', key: 'carbs' },
    { title: 'Protein (g)', align: 'end', key: 'protein' },
    { title: 'Iron (%)', align: 'end', key: 'iron' },
  ])
  const desserts = ref([
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ])
</script>

<script>
  export default {
    data () {
      return {
        selected: [],
        headers: [
          {
            title: 'Dessert (100g serving)',
            align: 'start',
            key: 'name',
          },
          { title: 'Calories', align: 'end', key: 'calories' },
          { title: 'Fat (g)', align: 'end', key: 'fat' },
          { title: 'Carbs (g)', align: 'end', key: 'carbs' },
          { title: 'Protein (g)', align: 'end', key: 'protein' },
          { title: 'Iron (%)', align: 'end', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - prop select strategy

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    item-value="name"
    select-strategy="single"
    show-select
  ></v-data-table>
</template>

<script setup>
  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      key: 'name',
    },
    { title: 'Calories', align: 'end', key: 'calories' },
    { title: 'Fat (g)', align: 'end', key: 'fat' },
    { title: 'Carbs (g)', align: 'end', key: 'carbs' },
    { title: 'Protein (g)', align: 'end', key: 'protein' },
    { title: 'Iron (%)', align: 'end', key: 'iron' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            title: 'Dessert (100g serving)',
            align: 'start',
            key: 'name',
          },
          { title: 'Calories', align: 'end', key: 'calories' },
          { title: 'Fat (g)', align: 'end', key: 'fat' },
          { title: 'Carbs (g)', align: 'end', key: 'carbs' },
          { title: 'Protein (g)', align: 'end', key: 'protein' },
          { title: 'Iron (%)', align: 'end', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - misc edit dialog

Example code

```vue
<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="desserts"
    >
      <template v-slot:item.name="props">
        <v-edit-dialog
          v-model:return-value="props.item.name"
          @cancel="cancel"
          @close="close"
          @open="open"
          @save="save"
        >
          {{ props.item.name }}
          <template v-slot:input>
            <v-text-field
              v-model="props.item.name"
              :rules="[max25chars]"
              label="Edit"
              counter
              single-line
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template v-slot:item.iron="props">
        <v-edit-dialog
          v-model:return-value="props.item.iron"
          large
          persistent
          @cancel="cancel"
          @close="close"
          @open="open"
          @save="save"
        >
          <div>{{ props.item.iron }}</div>
          <template v-slot:input>
            <div class="mt-4 text-h6">
              Update Iron
            </div>
            <v-text-field
              v-model="props.item.iron"
              :rules="[max25chars]"
              label="Edit"
              autofocus
              counter
              single-line
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
    </v-data-table>

    <v-snackbar
      v-model="snack"
      :color="snackColor"
      :timeout="3000"
    >
      {{ snackText }}

      <template v-slot:actions>
        <v-btn @click="snack = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const snack = ref(false)
  const snackColor = ref('')
  const snackText = ref('')
  const max25chars = ref(v => v.length <= 25 || 'Input too long!')
  const headers = ref([
    {
      text: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      value: 'name',
    },
    { text: 'Calories', value: 'calories' },
    { text: 'Fat (g)', value: 'fat' },
    { text: 'Carbs (g)', value: 'carbs' },
    { text: 'Protein (g)', value: 'protein' },
    { text: 'Iron (%)', value: 'iron' },
  ])
  const desserts = ref([
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ])
  function save () {
    snack.value = true
    snackColor.value = 'success'
    snackText.value = 'Data saved'
  }
  function cancel () {
    snack.value = true
    snackColor.value = 'error'
    snackText.value = 'Canceled'
  }
  function open () {
    snack.value = true
    snackColor.value = 'info'
    snackText.value = 'Dialog opened'
  }
  function close () {
    console.log('Dialog closed')
  }
</script>

<script>
  export default {
    data () {
      return {
        snack: false,
        snackColor: '',
        snackText: '',
        max25chars: v => v.length <= 25 || 'Input too long!',
        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
    methods: {
      save () {
        this.snack = true
        this.snackColor = 'success'
        this.snackText = 'Data saved'
      },
      cancel () {
        this.snack = true
        this.snackColor = 'error'
        this.snackText = 'Canceled'
      },
      open () {
        this.snack = true
        this.snackColor = 'info'
        this.snackText = 'Dialog opened'
      },
      close () {
        console.log('Dialog closed')
      },
    },
  }
</script>

```

# Vuetify component v-data-table - slot main

Example code

```vue
<template>
  <div>
    <v-select
      v-model="enabled"
      :items="slots"
      label="Slot"
      clearable
    ></v-select>
    <v-data-table
      :headers="headerArray"
      :hide-default-header="hideHeaders"
      :items="itemsArray"
      :loading="isLoading"
      :search="search"
      :show-select="showSelect"
      class="elevation-1"
      item-key="name"
      hide-default-footer
    >
      <template
        v-if="isEnabled('top')"
        v-slot:top
      >
        <div>This is content above the actual table</div>
      </template>

      <template
        v-if="isEnabled('header.data-table-select')"
        v-slot:header.data-table-select="{ on, props }"
      >
        <v-checkbox-btn
          color="purple"
          v-bind="props"
          v-on="on"
        ></v-checkbox-btn>
      </template>

      <template
        v-if="isEnabled('header')"
        v-slot:header="{ props: { headers } }"
      >
        <thead>
          <tr>
            <th :colspan="headers.length">
              This is a header
            </th>
          </tr>
        </thead>
      </template>

      <template
        v-if="isEnabled('progress')"
        v-slot:progress
      >
        <v-progress-linear
          :height="10"
          color="purple"
          indeterminate
        ></v-progress-linear>
      </template>

      <template
        v-if="isEnabled('item.data-table-select')"
        v-slot:item.data-table-select="{ isSelected, select }"
      >
        <v-checkbox-btn
          :value="isSelected"
          color="green"
          @input="select($event)"
        ></v-checkbox-btn>
      </template>

      <template
        v-if="isEnabled('item.<name>')"
        v-slot:item.name="{ value }"
      >
        {{ value.toUpperCase() }}
      </template>

      <template
        v-if="isEnabled('body.prepend')"
        v-slot:body.prepend="{ headers }"
      >
        <tr>
          <td :colspan="headers.length">
            This is a prepended row
          </td>
        </tr>
      </template>

      <template
        v-if="isEnabled('body')"
        v-slot:body="{ items }"
      >
        <tbody>
          <tr
            v-for="item in items"
            :key="item.raw.name"
          >
            <td>{{ item.raw.name }}</td>
            <td>CONTENT</td>
            <td>CONTENT</td>
            <td>CONTENT</td>
            <td>CONTENT</td>
            <td>CONTENT</td>
          </tr>
        </tbody>
      </template>

      <template
        v-if="isEnabled('no-data')"
        v-slot:no-data
      >
        NO DATA HERE!
      </template>

      <template
        v-if="isEnabled('no-results')"
        v-slot:no-results
      >
        NO RESULTS HERE!
      </template>

      <template
        v-if="isEnabled('body.append')"
        v-slot:body.append="{ headers }"
      >
        <tr>
          <td :colspan="headers.length">
            This is an appended row
          </td>
        </tr>
      </template>

      <template
        v-if="isEnabled('footer')"
        v-slot:footer
      >
        <div>
          This is a footer
        </div>
      </template>
    </v-data-table>
  </div>
</template>

<script>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6.0,
      carbs: 24,
      protein: 4.0,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9.0,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16.0,
      carbs: 23,
      protein: 6.0,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16.0,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0.0,
      carbs: 94,
      protein: 0.0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25.0,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26.0,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]

  export default {
    data () {
      return {
        enabled: null,
        itemsArray: desserts,
        search: null,
        slots: [
          'body',
          'body.append',
          'body.prepend',
          'footer',
          'header.data-table-select',
          'header',
          'progress',
          'item.data-table-select',
          'item.<name>',
          'no-data',
          'no-results',
          'top',
        ],
        headerArray: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
      }
    },

    computed: {
      showSelect () {
        return this.isEnabled('header.data-table-select') || this.isEnabled('item.data-table-select')
      },
      hideHeaders () {
        return !this.showSelect
      },
      isLoading () {
        return this.isEnabled('progress')
      },
    },

    watch: {
      enabled (slot) {
        if (slot === 'no-data') {
          this.items = []
        } else if (slot === 'no-results') {
          this.search = '...'
        } else {
          this.search = null
          this.itemsArray = desserts
        }
      },
    },

    methods: {
      isEnabled (slot) {
        return this.enabled === slot
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop headers sort raw

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="items"
  ></v-data-table>
</template>

<script setup>
  function sortRaw (a, b) {
    if (a.location < b.location) return -1
    if (a.location > b.location) return 1

    const dateA = a.constructed.split('-').pop().trim()
    const dateB = b.constructed.split('-').pop().trim()

    return dateA.localeCompare(dateB, undefined, { numeric: true, sensitivity: 'base' })
  }

  const headers = [
    { title: 'Name', key: 'name' },
    { title: 'Location', key: 'location', sortRaw },
    { title: 'Constructed', key: 'constructed' },
    { title: 'Description', key: 'description' },
  ]

  const items = [
    { name: 'Great Pyramid of Giza', location: 'Egypt', constructed: '2584-2561 BC', description: 'The oldest and largest of the three pyramids in the Giza pyramid complex.' },
    { name: 'Hanging Gardens of Babylon', location: 'Iraq', constructed: '600 BC', description: 'An ascending series of tiered gardens, said to have been built in ancient Babylon.' },
    { name: 'Statue of Zeus at Olympia', location: 'Greece', constructed: '435 BC', description: 'A giant seated figure of Zeus, made by the sculptor Phidias.' },
    { name: 'Temple of Artemis at Ephesus', location: 'Turkey', constructed: '550 BC', description: 'A large temple dedicated to the goddess Artemis, one of the Seven Wonders of the Ancient World.' },
    { name: 'Mausoleum at Halicarnassus', location: 'Turkey', constructed: '351 BC', description: 'A tomb built for Mausolus, a satrap of the Persian Empire.' },
    { name: 'Colossus of Rhodes', location: 'Greece', constructed: '292-280 BC', description: 'A statue of the Greek sun-god Helios, erected in the city of Rhodes.' },
    { name: 'Lighthouse of Alexandria', location: 'Egypt', constructed: '280 BC', description: 'A lighthouse built by the Ptolemaic Kingdom on the island of Pharos.' },
    { name: 'Great Wall of China', location: 'China', constructed: '7th century BC - 1644 AD', description: 'A series of fortifications made of stone, brick, and other materials.' },
    { name: 'Petra', location: 'Jordan', constructed: '312 BC', description: 'A historical city known for its rock-cut architecture and water conduit system.' },
    { name: 'Taj Mahal', location: 'India', constructed: '1632-1653 AD', description: 'An ivory-white marble mausoleum on the south bank of the Yamuna river.' },
    { name: 'Machu Picchu', location: 'Peru', constructed: '1450 AD', description: 'An Incan citadel set high in the Andes Mountains.' },
    { name: 'Chichen Itza', location: 'Mexico', constructed: '600 AD', description: 'A large pre-Columbian archaeological site built by the Maya people.' },
    { name: 'Roman Colosseum', location: 'Italy', constructed: '70-80 AD', description: 'An oval amphitheatre in the centre of the city of Rome.' },
    { name: 'Stonehenge', location: 'United Kingdom', constructed: '3000 BC - 2000 BC', description: 'A prehistoric monument consisting of a ring of standing stones.' },
    { name: 'Angkor Wat', location: 'Cambodia', constructed: '12th century AD', description: 'The largest religious monument in the world, originally constructed as a Hindu temple.' },
    { name: 'Moai Statues of Easter Island', location: 'Chile', constructed: '1250-1500 AD', description: 'Monolithic human figures carved by the Rapa Nui people on Easter Island.' },
    { name: 'Hagia Sophia', location: 'Turkey', constructed: '537 AD', description: 'A former Greek Orthodox Christian patriarchal basilica, later an Ottoman imperial mosque and now a museum.' },
    { name: 'Alhambra', location: 'Spain', constructed: '13th century AD', description: 'A palace and fortress complex located in Granada.' },
    { name: 'Forbidden City', location: 'China', constructed: '1406-1420 AD', description: 'A palace complex in central Beijing, serving as the home of emperors and their households.' },
    { name: 'Christ the Redeemer', location: 'Brazil', constructed: '1922-1931 AD', description: 'An Art Deco statue of Jesus Christ in Rio de Janeiro.' },
    { name: 'Acropolis of Athens', location: 'Greece', constructed: '5th century BC', description: 'An ancient citadel located on a rocky outcrop above the city of Athens.' },
    { name: 'Terracotta Army', location: 'China', constructed: '246-206 BC', description: 'A collection of terracotta sculptures depicting the armies of Qin Shi Huang, the first Emperor of China.' },
    { name: 'Parthenon', location: 'Greece', constructed: '447-438 BC', description: 'A former temple on the Athenian Acropolis, dedicated to the goddess Athena.' },
    { name: 'Tower of London', location: 'United Kingdom', constructed: '1078 AD', description: 'A historic castle located on the north bank of the River Thames in central London.' },
    { name: 'Neuschwanstein Castle', location: 'Germany', constructed: '1869-1886 AD', description: 'A 19th-century Romanesque Revival palace on a rugged hill above the village of Hohenschwangau.' },
  ]
</script>

<script>
  export default {
    data: () => ({
      headers: [
        { title: 'Name', key: 'name' },
        {
          title: 'Location',
          key: 'location',
          sortRaw (a, b) {
            if (a.location < b.location) return -1
            if (a.location > b.location) return 1

            const dateA = a.constructed.split('-').pop().trim()
            const dateB = b.constructed.split('-').pop().trim()

            return dateA.localeCompare(dateB, undefined, { numeric: true, sensitivity: 'base' })
          },
        },
        { title: 'Constructed', key: 'constructed' },
        { title: 'Description', key: 'description' },
      ],
      items: [
        { name: 'Great Pyramid of Giza', location: 'Egypt', constructed: '2584-2561 BC', description: 'The oldest and largest of the three pyramids in the Giza pyramid complex.' },
        { name: 'Hanging Gardens of Babylon', location: 'Iraq', constructed: '600 BC', description: 'An ascending series of tiered gardens, said to have been built in ancient Babylon.' },
        { name: 'Statue of Zeus at Olympia', location: 'Greece', constructed: '435 BC', description: 'A giant seated figure of Zeus, made by the sculptor Phidias.' },
        { name: 'Temple of Artemis at Ephesus', location: 'Turkey', constructed: '550 BC', description: 'A large temple dedicated to the goddess Artemis, one of the Seven Wonders of the Ancient World.' },
        { name: 'Mausoleum at Halicarnassus', location: 'Turkey', constructed: '351 BC', description: 'A tomb built for Mausolus, a satrap of the Persian Empire.' },
        { name: 'Colossus of Rhodes', location: 'Greece', constructed: '292-280 BC', description: 'A statue of the Greek sun-god Helios, erected in the city of Rhodes.' },
        { name: 'Lighthouse of Alexandria', location: 'Egypt', constructed: '280 BC', description: 'A lighthouse built by the Ptolemaic Kingdom on the island of Pharos.' },
        { name: 'Great Wall of China', location: 'China', constructed: '7th century BC - 1644 AD', description: 'A series of fortifications made of stone, brick, and other materials.' },
        { name: 'Petra', location: 'Jordan', constructed: '312 BC', description: 'A historical city known for its rock-cut architecture and water conduit system.' },
        { name: 'Taj Mahal', location: 'India', constructed: '1632-1653 AD', description: 'An ivory-white marble mausoleum on the south bank of the Yamuna river.' },
        { name: 'Machu Picchu', location: 'Peru', constructed: '1450 AD', description: 'An Incan citadel set high in the Andes Mountains.' },
        { name: 'Chichen Itza', location: 'Mexico', constructed: '600 AD', description: 'A large pre-Columbian archaeological site built by the Maya people.' },
        { name: 'Roman Colosseum', location: 'Italy', constructed: '70-80 AD', description: 'An oval amphitheatre in the centre of the city of Rome.' },
        { name: 'Stonehenge', location: 'United Kingdom', constructed: '3000 BC - 2000 BC', description: 'A prehistoric monument consisting of a ring of standing stones.' },
        { name: 'Angkor Wat', location: 'Cambodia', constructed: '12th century AD', description: 'The largest religious monument in the world, originally constructed as a Hindu temple.' },
        { name: 'Moai Statues of Easter Island', location: 'Chile', constructed: '1250-1500 AD', description: 'Monolithic human figures carved by the Rapa Nui people on Easter Island.' },
        { name: 'Hagia Sophia', location: 'Turkey', constructed: '537 AD', description: 'A former Greek Orthodox Christian patriarchal basilica, later an Ottoman imperial mosque and now a museum.' },
        { name: 'Alhambra', location: 'Spain', constructed: '13th century AD', description: 'A palace and fortress complex located in Granada.' },
        { name: 'Forbidden City', location: 'China', constructed: '1406-1420 AD', description: 'A palace complex in central Beijing, serving as the home of emperors and their households.' },
        { name: 'Christ the Redeemer', location: 'Brazil', constructed: '1922-1931 AD', description: 'An Art Deco statue of Jesus Christ in Rio de Janeiro.' },
        { name: 'Acropolis of Athens', location: 'Greece', constructed: '5th century BC', description: 'An ancient citadel located on a rocky outcrop above the city of Athens.' },
        { name: 'Terracotta Army', location: 'China', constructed: '246-206 BC', description: 'A collection of terracotta sculptures depicting the armies of Qin Shi Huang, the first Emperor of China.' },
        { name: 'Parthenon', location: 'Greece', constructed: '447-438 BC', description: 'A former temple on the Athenian Acropolis, dedicated to the goddess Athena.' },
        { name: 'Tower of London', location: 'United Kingdom', constructed: '1078 AD', description: 'A historic castle located on the north bank of the River Thames in central London.' },
        { name: 'Neuschwanstein Castle', location: 'Germany', constructed: '1869-1886 AD', description: 'A 19th-century Romanesque Revival palace on a rugged hill above the village of Hohenschwangau.' },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - server

Example code

```vue
<template>
  <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    :items-length="totalItems"
    :loading="loading"
    item-value="name"
    @update:options="loadItems"
  ></v-data-table-server>
</template>

<script setup>
  import { ref } from 'vue'

  const cars = [
    {
      name: 'Ford Mustang',
      horsepower: 450,
      fuel: 'Gasoline',
      origin: 'USA',
      price: 55000,
    },
    {
      name: 'Tesla Model S',
      horsepower: 670,
      fuel: 'Electric',
      origin: 'USA',
      price: 79999,
    },
    {
      name: 'BMW M3',
      horsepower: 503,
      fuel: 'Gasoline',
      origin: 'Germany',
      price: 70000,
    },
    {
      name: 'Audi RS6',
      horsepower: 591,
      fuel: 'Gasoline',
      origin: 'Germany',
      price: 109000,
    },
    {
      name: 'Chevrolet Camaro',
      horsepower: 650,
      fuel: 'Gasoline',
      origin: 'USA',
      price: 62000,
    },
    {
      name: 'Porsche 911',
      horsepower: 379,
      fuel: 'Gasoline',
      origin: 'Germany',
      price: 101000,
    },
    {
      name: 'Jaguar F-Type',
      horsepower: 575,
      fuel: 'Gasoline',
      origin: 'UK',
      price: 61000,
    },
    {
      name: 'Mazda MX-5',
      horsepower: 181,
      fuel: 'Gasoline',
      origin: 'Japan',
      price: 26000,
    },
    {
      name: 'Nissan GT-R',
      horsepower: 565,
      fuel: 'Gasoline',
      origin: 'Japan',
      price: 113540,
    },
    {
      name: 'Mercedes-AMG GT',
      horsepower: 523,
      fuel: 'Gasoline',
      origin: 'Germany',
      price: 115900,
    },
  ]

  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = cars.slice()
          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }
          const paginated = items.slice(start, end)
          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }
  const itemsPerPage = ref(5)
  const headers = ref([
    { title: 'Car Model', key: 'name', align: 'start' },
    { title: 'Horsepower', key: 'horsepower', align: 'end' },
    { title: 'Fuel Type', key: 'fuel', align: 'start' },
    { title: 'Origin', key: 'origin', align: 'start' },
    { title: 'Price ($)', key: 'price', align: 'end' },
  ])
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
    FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
      serverItems.value = items
      totalItems.value = total
      loading.value = false
    })
  }
</script>

<script>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6.0,
      carbs: 24,
      protein: 4.0,
      iron: '1',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0.0,
      carbs: 94,
      protein: 0.0,
      iron: '0',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26.0,
      carbs: 65,
      protein: 7,
      iron: '6',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16.0,
      carbs: 23,
      protein: 6.0,
      iron: '7',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16.0,
      carbs: 49,
      protein: 3.9,
      iron: '16',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9.0,
      carbs: 37,
      protein: 4.3,
      iron: '1',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25.0,
      carbs: 51,
      protein: 4.9,
      iron: '22',
    },
  ]

  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice()

          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }

          const paginated = items.slice(start, end)

          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }

  export default {
    data: () => ({
      itemsPerPage: 5,
      headers: [
        {
          title: 'Dessert (100g serving)',
          align: 'start',
          sortable: false,
          key: 'name',
        },
        { title: 'Calories', key: 'calories', align: 'end' },
        { title: 'Fat (g)', key: 'fat', align: 'end' },
        { title: 'Carbs (g)', key: 'carbs', align: 'end' },
        { title: 'Protein (g)', key: 'protein', align: 'end' },
        { title: 'Iron (%)', key: 'iron', align: 'end' },
      ],
      serverItems: [],
      loading: true,
      totalItems: 0,
    }),
    methods: {
      loadItems ({ page, itemsPerPage, sortBy }) {
        this.loading = true
        FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
          this.serverItems = items
          this.totalItems = total
          this.loading = false
        })
      },
    },
  }
</script>

```

# Vuetify component v-data-table - slot item key

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="vegetables"
  >
    <template v-slot:item.calories="{ value }">
      <v-chip
        :border="`${getColor(value)} thin opacity-25`"
        :color="getColor(value)"
        :text="value"
        size="x-small"
      ></v-chip>
    </template>
  </v-data-table>
</template>

<script setup>
  const headers = [
    { title: 'Vegetable', key: 'name' },
    { title: 'Calories', key: 'calories' },
    { title: 'Fat(g)', key: 'fat' },
    { title: 'Carbs(g)', key: 'carbs' },
    { title: 'Protein(g)', key: 'protein' },
    { title: 'Iron(%)', key: 'iron' },
  ]
  const vegetables = [
    {
      name: 'Spinach',
      calories: 23,
      fat: 0.4,
      carbs: 3.6,
      protein: 2.9,
      iron: '15%',
    },
    {
      name: 'Kael',
      calories: 49,
      fat: 0.9,
      carbs: 8.8,
      protein: 4.3,
      iron: '16%',
    },
    {
      name: 'Broccoli',
      calories: 34,
      fat: 0.4,
      carbs: 6.6,
      protein: 2.8,
      iron: '6%',
    },
    {
      name: 'Brussels Sprouts',
      calories: 43,
      fat: 0.3,
      carbs: 8.9,
      protein: 3.4,
      iron: '9%',
    },
    {
      name: 'Avocado',
      calories: 160,
      fat: 15,
      carbs: 9,
      protein: 2,
      iron: '3%',
    },
    {
      name: 'Sweet Potato',
      calories: 86,
      fat: 0.1,
      carbs: 20.1,
      protein: 1.6,
      iron: '3%',
    },
    {
      name: 'Corn',
      calories: 96,
      fat: 1.5,
      carbs: 21,
      protein: 3.4,
      iron: '2%',
    },
    {
      name: 'Potato',
      calories: 77,
      fat: 0.1,
      carbs: 17.5,
      protein: 2,
      iron: '8%',
    },
    {
      name: 'Butternut Squash',
      calories: 45,
      fat: 0.1,
      carbs: 11.7,
      protein: 1,
      iron: '4%',
    },
    {
      name: 'Beetroot',
      calories: 43,
      fat: 0.2,
      carbs: 10,
      protein: 1.6,
      iron: '6%',
    },
    {
      name: 'Parsnip',
      calories: 75,
      fat: 0.3,
      carbs: 18,
      protein: 1.2,
      iron: '4%',
    },
    {
      name: 'Yam',
      calories: 118,
      fat: 0.2,
      carbs: 27.9,
      protein: 1.5,
      iron: '4%',
    },
    {
      name: 'Acorn Squash',
      calories: 40,
      fat: 0.1,
      carbs: 10,
      protein: 1,
      iron: '5%',
    },
    {
      name: 'Artichoke',
      calories: 47,
      fat: 0.2,
      carbs: 10.5,
      protein: 3.3,
      iron: '7%',
    },
    {
      name: 'Peas',
      calories: 81,
      fat: 0.4,
      carbs: 14.5,
      protein: 5.4,
      iron: '25%',
    },
    {
      name: 'Green Beans',
      calories: 31,
      fat: 0.1,
      carbs: 6.9,
      protein: 1.8,
      iron: '8%',
    },
    {
      name: 'Red Bell Pepper',
      calories: 26,
      fat: 0.2,
      carbs: 6.0,
      protein: 1.0,
      iron: '3%',
    },
    {
      name: 'Cauliflower',
      calories: 25,
      fat: 0.1,
      carbs: 5.0,
      protein: 1.9,
      iron: '4%',
    },
    {
      name: 'Zucchini',
      calories: 17,
      fat: 0.3,
      carbs: 3.1,
      protein: 1.2,
      iron: '3%',
    },
    {
      name: 'Asparagus',
      calories: 20,
      fat: 0.1,
      carbs: 3.9,
      protein: 2.2,
      iron: '16%',
    },
    {
      name: 'Eggplant',
      calories: 25,
      fat: 0.2,
      carbs: 6,
      protein: 1,
      iron: '1%',
    },
    {
      name: 'Pumpkin',
      calories: 26,
      fat: 0.1,
      carbs: 6.5,
      protein: 1,
      iron: '4%',
    },
    {
      name: 'Celery',
      calories: 16,
      fat: 0.2,
      carbs: 3,
      protein: 0.7,
      iron: '1%',
    },
    {
      name: 'Cucumber',
      calories: 15,
      fat: 0.1,
      carbs: 3.6,
      protein: 0.7,
      iron: '2%',
    },
    {
      name: 'Leek',
      calories: 61,
      fat: 0.3,
      carbs: 14.2,
      protein: 1.5,
      iron: '12%',
    },
    {
      name: 'Fennel',
      calories: 31,
      fat: 0.2,
      carbs: 7,
      protein: 1.2,
      iron: '6%',
    },
    {
      name: 'Green Peas',
      calories: 81,
      fat: 0.4,
      carbs: 14.5,
      protein: 5.4,
      iron: '25%',
    },
    {
      name: 'Okra',
      calories: 33,
      fat: 0.2,
      carbs: 7.5,
      protein: 1.9,
      iron: '3%',
    },
    {
      name: 'Chard',
      calories: 19,
      fat: 0.2,
      carbs: 3.7,
      protein: 1.8,
      iron: '22%',
    },
    {
      name: 'Collard Greens',
      calories: 32,
      fat: 0.6,
      carbs: 5.4,
      protein: 3,
      iron: '2%',
    },
  ]

  function getColor (calories) {
    if (calories > 100) return 'error'
    else if (calories > 50) return 'warning'
    else return 'success'
  }
</script>

<script>
  export default {
    data: () => ({
      headers: [
        { title: 'Vegetable', key: 'name' },
        { title: 'Calories', key: 'calories' },
        { title: 'Fat(g)', key: 'fat' },
        { title: 'Carbs(g)', key: 'carbs' },
        { title: 'Protein(g)', key: 'protein' },
        { title: 'Iron(%)', key: 'iron' },
      ],
      vegetables: [
        {
          name: 'Spinach',
          calories: 23,
          fat: 0.4,
          carbs: 3.6,
          protein: 2.9,
          iron: '15%',
        },
        {
          name: 'Kael',
          calories: 49,
          fat: 0.9,
          carbs: 8.8,
          protein: 4.3,
          iron: '16%',
        },
        {
          name: 'Broccoli',
          calories: 34,
          fat: 0.4,
          carbs: 6.6,
          protein: 2.8,
          iron: '6%',
        },
        {
          name: 'Brussels Sprouts',
          calories: 43,
          fat: 0.3,
          carbs: 8.9,
          protein: 3.4,
          iron: '9%',
        },
        {
          name: 'Avocado',
          calories: 160,
          fat: 15,
          carbs: 9,
          protein: 2,
          iron: '3%',
        },
        {
          name: 'Sweet Potato',
          calories: 86,
          fat: 0.1,
          carbs: 20.1,
          protein: 1.6,
          iron: '3%',
        },
        {
          name: 'Corn',
          calories: 96,
          fat: 1.5,
          carbs: 21,
          protein: 3.4,
          iron: '2%',
        },
        {
          name: 'Potato',
          calories: 77,
          fat: 0.1,
          carbs: 17.5,
          protein: 2,
          iron: '8%',
        },
        {
          name: 'Butternut Squash',
          calories: 45,
          fat: 0.1,
          carbs: 11.7,
          protein: 1,
          iron: '4%',
        },
        {
          name: 'Beetroot',
          calories: 43,
          fat: 0.2,
          carbs: 10,
          protein: 1.6,
          iron: '6%',
        },
        {
          name: 'Parsnip',
          calories: 75,
          fat: 0.3,
          carbs: 18,
          protein: 1.2,
          iron: '4%',
        },
        {
          name: 'Yam',
          calories: 118,
          fat: 0.2,
          carbs: 27.9,
          protein: 1.5,
          iron: '4%',
        },
        {
          name: 'Acorn Squash',
          calories: 40,
          fat: 0.1,
          carbs: 10,
          protein: 1,
          iron: '5%',
        },
        {
          name: 'Artichoke',
          calories: 47,
          fat: 0.2,
          carbs: 10.5,
          protein: 3.3,
          iron: '7%',
        },
        {
          name: 'Peas',
          calories: 81,
          fat: 0.4,
          carbs: 14.5,
          protein: 5.4,
          iron: '25%',
        },
        {
          name: 'Green Beans',
          calories: 31,
          fat: 0.1,
          carbs: 6.9,
          protein: 1.8,
          iron: '8%',
        },
        {
          name: 'Red Bell Pepper',
          calories: 26,
          fat: 0.2,
          carbs: 6.0,
          protein: 1.0,
          iron: '3%',
        },
        {
          name: 'Cauliflower',
          calories: 25,
          fat: 0.1,
          carbs: 5.0,
          protein: 1.9,
          iron: '4%',
        },
        {
          name: 'Zucchini',
          calories: 17,
          fat: 0.3,
          carbs: 3.1,
          protein: 1.2,
          iron: '3%',
        },
        {
          name: 'Asparagus',
          calories: 20,
          fat: 0.1,
          carbs: 3.9,
          protein: 2.2,
          iron: '16%',
        },
        {
          name: 'Eggplant',
          calories: 25,
          fat: 0.2,
          carbs: 6,
          protein: 1,
          iron: '1%',
        },
        {
          name: 'Pumpkin',
          calories: 26,
          fat: 0.1,
          carbs: 6.5,
          protein: 1,
          iron: '4%',
        },
        {
          name: 'Celery',
          calories: 16,
          fat: 0.2,
          carbs: 3,
          protein: 0.7,
          iron: '1%',
        },
        {
          name: 'Cucumber',
          calories: 15,
          fat: 0.1,
          carbs: 3.6,
          protein: 0.7,
          iron: '2%',
        },
        {
          name: 'Leek',
          calories: 61,
          fat: 0.3,
          carbs: 14.2,
          protein: 1.5,
          iron: '12%',
        },
        {
          name: 'Fennel',
          calories: 31,
          fat: 0.2,
          carbs: 7,
          protein: 1.2,
          iron: '6%',
        },
        {
          name: 'Green Peas',
          calories: 81,
          fat: 0.4,
          carbs: 14.5,
          protein: 5.4,
          iron: '25%',
        },
        {
          name: 'Okra',
          calories: 33,
          fat: 0.2,
          carbs: 7.5,
          protein: 1.9,
          iron: '3%',
        },
        {
          name: 'Chard',
          calories: 19,
          fat: 0.2,
          carbs: 3.7,
          protein: 1.8,
          iron: '22%',
        },
        {
          name: 'Collard Greens',
          calories: 32,
          fat: 0.6,
          carbs: 5.4,
          protein: 3,
          iron: '2%',
        },
      ],
    }),

    methods: {
      getColor (calories) {
        if (calories > 100) return 'error'
        else if (calories > 50) return 'warning'
        else return 'success'
      },
    },
  }
</script>

```

# Vuetify component v-data-table - misc external paginate

Example code

```vue
<template>
  <v-data-table
    v-model:page="page"
    :headers="headers"
    :items="desserts"
    :items-per-page="itemsPerPage"
  >
    <template v-slot:top>
      <v-text-field
        :model-value="itemsPerPage"
        class="pa-2"
        label="Items per page"
        max="15"
        min="-1"
        type="number"
        hide-details
        @update:model-value="itemsPerPage = parseInt($event, 10)"
      ></v-text-field>
    </template>

    <template v-slot:bottom>
      <div class="text-center pt-2">
        <v-pagination
          v-model="page"
          :length="pageCount"
        ></v-pagination>
      </div>
    </template>
  </v-data-table>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const page = ref(1)
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      align: 'start',
      key: 'name',
      sortable: false,
      title: 'Dessert (100g serving)',
    },
    { title: 'Calories', key: 'calories' },
    { title: 'Fat (g)', key: 'fat' },
    { title: 'Carbs (g)', key: 'carbs' },
    { title: 'Protein (g)', key: 'protein' },
    { title: 'Iron (%)', key: 'iron' },
  ])
  const desserts = ref([
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ])
  const pageCount = computed(() => {
    return Math.ceil(desserts.value.length / itemsPerPage.value)
  })
</script>

<script>
  export default {
    data () {
      return {
        page: 1,
        itemsPerPage: 5,
        headers: [
          {
            align: 'start',
            key: 'name',
            sortable: false,
            title: 'Dessert (100g serving)',
          },
          { title: 'Calories', key: 'calories' },
          { title: 'Fat (g)', key: 'fat' },
          { title: 'Carbs (g)', key: 'carbs' },
          { title: 'Protein (g)', key: 'protein' },
          { title: 'Iron (%)', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
    computed: {
      pageCount () {
        return Math.ceil(this.desserts.length / this.itemsPerPage)
      },
    },
  }
</script>

```

# Vuetify component v-data-table - slot group header

Example code

```vue
<template>
  <v-data-table
    :group-by="groupBy"
    :headers="headers"
    :items="tools"
    item-value="name"
    hide-default-footer
  >
    <template v-slot:group-header="{ item, columns, toggleGroup, isGroupOpen }">
      <tr>
        <td :colspan="columns.length">
          <div class="d-flex align-center">
            <v-btn
              :icon="isGroupOpen(item) ? '$expand' : '$next'"
              color="medium-emphasis"
              density="comfortable"
              size="small"
              variant="outlined"
              @click="toggleGroup(item)"
            ></v-btn>

            <span class="ms-4">Tool Type: {{ item.value }}</span>
          </div>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>

<script setup>
  const groupBy = [{ key: 'type', order: 'asc' }]

  const headers = [
    {
      title: 'Tool Name',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Weight(kg)', key: 'weight' },
    { title: 'Length(cm)', key: 'length' },
    { title: 'Price($)', key: 'price' },
  ]

  const tools = [
    {
      name: 'Hammer',
      weight: 0.5,
      length: 30,
      price: 10,
      type: 'hand',
    },
    {
      name: 'Screwdriver',
      weight: 0.2,
      length: 20,
      price: 5,
      type: 'hand',
    },
    {
      name: 'Drill',
      weight: 1.5,
      length: 25,
      price: 50,
      type: 'power',
    },
    {
      name: 'Saw',
      weight: 0.7,
      length: 50,
      price: 15,
      type: 'hand',
    },
    {
      name: 'Tape Measure',
      weight: 0.3,
      length: 10,
      price: 8,
      type: 'measuring',
    },
    {
      name: 'Level',
      weight: 0.4,
      length: 60,
      price: 12,
      type: 'measuring',
    },
    {
      name: 'Wrench',
      weight: 0.6,
      length: 25,
      price: 10,
      type: 'hand',
    },
    {
      name: 'Pliers',
      weight: 0.3,
      length: 15,
      price: 7,
      type: 'hand',
    },
    {
      name: 'Sander',
      weight: 2.0,
      length: 30,
      price: 60,
      type: 'power',
    },
    {
      name: 'Multimeter',
      weight: 0.5,
      length: 15,
      price: 30,
      type: 'measuring',
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        groupBy: [
          {
            key: 'gluten',
            order: 'asc',
          },
        ],
        headers: [
          {
            title: 'Tool Name',
            align: 'start',
            sortable: false,
            key: 'name',
          },
          { title: 'Weight (kg)', key: 'weight' },
          { title: 'Length (cm)', key: 'length' },
          { title: 'Price ($)', key: 'price' },
        ],
        tools: [
          {
            name: 'Hammer',
            weight: 0.5,
            length: 30,
            price: 10,
            type: 'hand',
          },
          {
            name: 'Screwdriver',
            weight: 0.2,
            length: 20,
            price: 5,
            type: 'hand',
          },
          {
            name: 'Drill',
            weight: 1.5,
            length: 25,
            price: 50,
            type: 'power',
          },
          {
            name: 'Saw',
            weight: 0.7,
            length: 50,
            price: 15,
            type: 'hand',
          },
          {
            name: 'Tape Measure',
            weight: 0.3,
            length: 10,
            price: 8,
            type: 'measuring',
          },
          {
            name: 'Level',
            weight: 0.4,
            length: 60,
            price: 12,
            type: 'measuring',
          },
          {
            name: 'Wrench',
            weight: 0.6,
            length: 25,
            price: 10,
            type: 'hand',
          },
          {
            name: 'Pliers',
            weight: 0.3,
            length: 15,
            price: 7,
            type: 'hand',
          },
          {
            name: 'Sander',
            weight: 2.0,
            length: 30,
            price: 60,
            type: 'power',
          },
          {
            name: 'Multimeter',
            weight: 0.5,
            length: 15,
            price: 30,
            type: 'measuring',
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - slot item data table select

Example code

```vue
<template>
  <v-data-table
    :items="desserts"
    item-value="name"
    show-select
  >
    <template v-slot:header.data-table-select="{ allSelected, selectAll, someSelected }">
      <v-checkbox-btn
        :indeterminate="someSelected && !allSelected"
        :model-value="allSelected"
        color="primary"
        @update:model-value="selectAll(!allSelected)"
      ></v-checkbox-btn>
    </template>

    <template v-slot:item.data-table-select="{ internalItem, isSelected, toggleSelect }">
      <v-checkbox-btn
        :model-value="isSelected(internalItem)"
        color="primary"
        @update:model-value="toggleSelect(internalItem)"
      ></v-checkbox-btn>
    </template>
  </v-data-table>
</template>

<script setup>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - misc external sort

Example code

```vue
<template>
  <div>
    <v-data-table
      v-model:sort-by="sortBy"
      :headers="headers"
      :items="desserts"
      class="elevation-1"
    ></v-data-table>
    <div class="text-center pt-2">
      <v-btn
        class="me-2"
        color="primary"
        @click="toggleOrder"
      >
        Toggle sort order
      </v-btn>
      <v-btn
        color="primary"
        @click="nextSort"
      >
        Sort next column
      </v-btn>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const sortBy = ref([{ key: 'fat', order: 'asc' }])
  const headers = ref([
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      key: 'name',
    },
    { title: 'Calories', key: 'calories' },
    { title: 'Fat (g)', key: 'fat' },
    { title: 'Carbs (g)', key: 'carbs' },
    { title: 'Protein (g)', key: 'protein' },
    { title: 'Iron (%)', key: 'iron' },
  ])
  const desserts = ref([
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ])
  function toggleOrder () {
    sortBy.value = [{ key: sortBy.value[0].key, order: sortBy.value[0].order === 'asc' ? 'desc' : 'asc' }]
  }
  function nextSort () {
    let index = headers.value.findIndex(h => h.key === sortBy.value[0].key)
    index = (index + 1) % headers.value.length
    sortBy.value = [{ key: headers.value[index].key, order: 'asc' }]
  }
</script>

<script>
  export default {
    data () {
      return {
        sortBy: [{ key: 'fat', order: 'asc' }],
        headers: [
          {
            title: 'Dessert (100g serving)',
            align: 'start',
            key: 'name',
          },
          { title: 'Calories', key: 'calories' },
          { title: 'Fat (g)', key: 'fat' },
          { title: 'Carbs (g)', key: 'carbs' },
          { title: 'Protein (g)', key: 'protein' },
          { title: 'Iron (%)', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
    methods: {
      toggleOrder () {
        this.sortBy = [{ key: this.sortBy[0].key, order: this.sortBy[0].order === 'asc' ? 'desc' : 'asc' }]
      },
      nextSort () {
        let index = this.headers.findIndex(h => h.key === this.sortBy[0].key)
        index = (index + 1) % this.headers.length
        this.sortBy = [{ key: this.headers[index].key, order: 'asc' }]
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop item value

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :item-value="item => `${item.name}-${item.version}`"
    :items="desserts"
    items-per-page="5"
    show-select
  ></v-data-table>
</template>

<script setup>
  const headers = [
    {
      title: 'Operating System',
      align: 'start',
      key: 'name',
    },
    { title: 'Version', align: 'end', key: 'version' },
  ]
  const desserts = [
    {
      name: 'Windows',
      version: '3.11',
    },
    {
      name: 'Windows',
      version: '95',
    },
    {
      name: 'Windows',
      version: '98',
    },
    {
      name: 'Windows',
      version: '2000',
    },
    {
      name: 'Windows',
      version: 'XP',
    },
    {
      name: 'Windows',
      version: 'Vista',
    },
    {
      name: 'Windows',
      version: '7',
    },
    {
      name: 'Windows',
      version: '8',
    },
    {
      name: 'Windows',
      version: '10',
    },
    {
      name: 'Windows',
      version: '11',
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            title: 'Operating System',
            align: 'start',
            key: 'name',
          },
          { title: 'Version', align: 'end', key: 'version' },
        ],
        desserts: [
          {
            name: 'Windows',
            version: '3.11',
          },
          {
            name: 'Windows',
            version: '95',
          },
          {
            name: 'Windows',
            version: '98',
          },
          {
            name: 'Windows',
            version: '2000',
          },
          {
            name: 'Windows',
            version: 'XP',
          },
          {
            name: 'Windows',
            version: 'Vista',
          },
          {
            name: 'Windows',
            version: '7',
          },
          {
            name: 'Windows',
            version: '8',
          },
          {
            name: 'Windows',
            version: '10',
          },
          {
            name: 'Windows',
            version: '11',
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - prop custom filter

Example code

```vue
<template>
  <v-data-table
    :custom-filter="filterOnlyCapsText"
    :headers="headers"
    :items="items"
    :search="search"
    item-value="name"
  >
    <template v-slot:top>
      <v-text-field
        v-model="search"
        class="pa-2"
        label="Search (UPPER CASE ONLY)"
      ></v-text-field>
    </template>
  </v-data-table>
</template>

<script setup>
  import { ref } from 'vue'

  const search = ref('')
  const headers = [
    {
      title: 'CPU Model',
      align: 'start',
      key: 'name',
    },
    {
      title: 'Cores',
      align: 'end',
      key: 'cores',
    },
    {
      title: 'Threads',
      align: 'end',
      key: 'threads',
    },
    {
      title: 'Base Clock',
      align: 'end',
      key: 'baseClock',
    },
    {
      title: 'Boost Clock',
      align: 'end',
      key: 'boostClock',
    },
    {
      title: 'TDP (W)',
      align: 'end',
      key: 'tdp',
    },
  ]
  const items = [
    {
      name: 'Intel Core i9-11900K',
      cores: 8,
      threads: 16,
      baseClock: '3.5 GHz',
      boostClock: '5.3 GHz',
      tdp: '125W',
    },
    {
      name: 'AMD Ryzen 9 5950X',
      cores: 16,
      threads: 32,
      baseClock: '3.4 GHz',
      boostClock: '4.9 GHz',
      tdp: '105W',
    },
    {
      name: 'Intel Core i7-10700K',
      cores: 8,
      threads: 16,
      baseClock: '3.8 GHz',
      boostClock: '5.1 GHz',
      tdp: '125W',
    },
    {
      name: 'AMD Ryzen 5 5600X',
      cores: 6,
      threads: 12,
      baseClock: '3.7 GHz',
      boostClock: '4.6 GHz',
      tdp: '65W',
    },
    {
      name: 'Intel Core i5-10600K',
      cores: 6,
      threads: 12,
      baseClock: '4.1 GHz',
      boostClock: '4.8 GHz',
      tdp: '125W',
    },
    {
      name: 'AMD Ryzen 7 5800X',
      cores: 8,
      threads: 16,
      baseClock: '3.8 GHz',
      boostClock: '4.7 GHz',
      tdp: '105W',
    },
    {
      name: 'Intel Core i3-10100',
      cores: 4,
      threads: 8,
      baseClock: '3.6 GHz',
      boostClock: '4.3 GHz',
      tdp: '65W',
    },
    {
      name: 'AMD Ryzen 3 3300X',
      cores: 4,
      threads: 8,
      baseClock: '3.8 GHz',
      boostClock: '4.3 GHz',
      tdp: '65W',
    },
    {
      name: 'Intel Pentium Gold G6400',
      cores: 2,
      threads: 4,
      baseClock: '4.0 GHz',
      tdp: '58W',
    },
    {
      name: 'AMD Athlon 3000G',
      cores: 2,
      threads: 4,
      baseClock: '3.5 GHz',
      tdp: '35W',
    },
  ]

  function filterOnlyCapsText (value, query, item) {
    return value != null && query != null && typeof value === 'string' && value.toString().toLocaleUpperCase().indexOf(query) !== -1
  }
</script>

<script>
  export default {
    data: () => ({
      search: '',
      headers: [
        {
          title: 'CPU Model',
          align: 'start',
          key: 'name',
        },
        {
          title: 'Cores',
          align: 'end',
          key: 'cores',
        },
        {
          title: 'Threads',
          align: 'end',
          key: 'threads',
        },
        {
          title: 'Base Clock',
          align: 'end',
          key: 'baseClock',
        },
        {
          title: 'Boost Clock',
          align: 'end',
          key: 'boostClock',
        },
        {
          title: 'TDP (W)',
          align: 'end',
          key: 'tdp',
        },
      ],
      items: [
        {
          name: 'Intel Core i9-11900K',
          cores: 8,
          threads: 16,
          baseClock: '3.5 GHz',
          boostClock: '5.3 GHz',
          tdp: '125W',
        },
        {
          name: 'AMD Ryzen 9 5950X',
          cores: 16,
          threads: 32,
          baseClock: '3.4 GHz',
          boostClock: '4.9 GHz',
          tdp: '105W',
        },
        {
          name: 'Intel Core i7-10700K',
          cores: 8,
          threads: 16,
          baseClock: '3.8 GHz',
          boostClock: '5.1 GHz',
          tdp: '125W',
        },
        {
          name: 'AMD Ryzen 5 5600X',
          cores: 6,
          threads: 12,
          baseClock: '3.7 GHz',
          boostClock: '4.6 GHz',
          tdp: '65W',
        },
        {
          name: 'Intel Core i5-10600K',
          cores: 6,
          threads: 12,
          baseClock: '4.1 GHz',
          boostClock: '4.8 GHz',
          tdp: '125W',
        },
        {
          name: 'AMD Ryzen 7 5800X',
          cores: 8,
          threads: 16,
          baseClock: '3.8 GHz',
          boostClock: '4.7 GHz',
          tdp: '105W',
        },
        {
          name: 'Intel Core i3-10100',
          cores: 4,
          threads: 8,
          baseClock: '3.6 GHz',
          boostClock: '4.3 GHz',
          tdp: '65W',
        },
        {
          name: 'AMD Ryzen 3 3300X',
          cores: 4,
          threads: 8,
          baseClock: '3.8 GHz',
          boostClock: '4.3 GHz',
          tdp: '65W',
        },
        {
          name: 'Intel Pentium Gold G6400',
          cores: 2,
          threads: 4,
          baseClock: '4.0 GHz',
          tdp: '58W',
        },
        {
          name: 'AMD Athlon 3000G',
          cores: 2,
          threads: 4,
          baseClock: '3.5 GHz',
          tdp: '35W',
        },
      ],
    }),

    methods: {
      filterOnlyCapsText (value, query, item) {
        return value != null &&
          query != null &&
          typeof value === 'string' &&
          value.toString().toLocaleUpperCase().indexOf(query) !== -1
      },
    },
  }
</script>

```

# Vuetify component v-data-table - server search

Example code

```vue
<template>
  <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    :items-length="totalItems"
    :loading="loading"
    :search="search"
    item-value="name"
    @update:options="loadItems"
  >
    <template v-slot:tfoot>
      <tr>
        <td>
          <v-text-field v-model="name" class="ma-2" density="compact" placeholder="Search name..." hide-details></v-text-field>
        </td>
        <td>
          <v-text-field
            v-model="calories"
            class="ma-2"
            density="compact"
            placeholder="Minimum calories"
            type="number"
            hide-details
          ></v-text-field>
        </td>
      </tr>
    </template>
  </v-data-table-server>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: '1',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: '0',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: '6',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: '7',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: '16',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: '1',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: '22',
    },
  ]
  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy, search }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice().filter(item => {
            if (search.name && !item.name.toLowerCase().includes(search.name.toLowerCase())) {
              return false
            }
            // eslint-disable-next-line sonarjs/prefer-single-boolean-return
            if (search.calories && !(item.calories >= Number(search.calories))) {
              return false
            }
            return true
          })
          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }
          const paginated = items.slice(start, end === -1 ? undefined : end)
          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }
  const itemsPerPage = ref(5)
  const headers = ref([
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Calories', key: 'calories', align: 'end' },
    { title: 'Fat (g)', key: 'fat', align: 'end' },
    { title: 'Carbs (g)', key: 'carbs', align: 'end' },
    { title: 'Protein (g)', key: 'protein', align: 'end' },
    { title: 'Iron (%)', key: 'iron', align: 'end' },
  ])
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  const name = ref('')
  const calories = ref('')
  const search = ref('')
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
    FakeAPI.fetch({ page, itemsPerPage, sortBy, search: { name: name.value, calories: calories.value } }).then(({ items, total }) => {
      serverItems.value = items
      totalItems.value = total
      loading.value = false
    })
  }
  watch(name, () => {
    search.value = String(Date.now())
  })
  watch(calories, () => {
    search.value = String(Date.now())
  })
</script>

<script>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6.0,
      carbs: 24,
      protein: 4.0,
      iron: '1',
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0.0,
      carbs: 94,
      protein: 0.0,
      iron: '0',
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26.0,
      carbs: 65,
      protein: 7,
      iron: '6',
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16.0,
      carbs: 23,
      protein: 6.0,
      iron: '7',
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16.0,
      carbs: 49,
      protein: 3.9,
      iron: '16',
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9.0,
      carbs: 37,
      protein: 4.3,
      iron: '1',
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: '2',
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: '8',
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: '45',
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25.0,
      carbs: 51,
      protein: 4.9,
      iron: '22',
    },
  ]

  const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy, search }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice().filter(item => {
            if (search.name && !item.name.toLowerCase().includes(search.name.toLowerCase())) {
              return false
            }

            // eslint-disable-next-line sonarjs/prefer-single-boolean-return
            if (search.calories && !(item.calories >= Number(search.calories))) {
              return false
            }

            return true
          })

          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }

          const paginated = items.slice(start, end)

          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }

  export default {
    data: () => ({
      itemsPerPage: 5,
      headers: [
        {
          title: 'Dessert (100g serving)',
          align: 'start',
          sortable: false,
          key: 'name',
        },
        { title: 'Calories', key: 'calories', align: 'end' },
        { title: 'Fat (g)', key: 'fat', align: 'end' },
        { title: 'Carbs (g)', key: 'carbs', align: 'end' },
        { title: 'Protein (g)', key: 'protein', align: 'end' },
        { title: 'Iron (%)', key: 'iron', align: 'end' },
      ],
      serverItems: [],
      loading: true,
      totalItems: 0,
      name: '',
      calories: '',
      search: '',
    }),
    watch: {
      name () {
        this.search = String(Date.now())
      },
      calories () {
        this.search = String(Date.now())
      },
    },
    methods: {
      loadItems ({ page, itemsPerPage, sortBy }) {
        this.loading = true
        FakeAPI.fetch({ page, itemsPerPage, sortBy, search: { name: this.name, calories: this.calories } }).then(({ items, total }) => {
          this.serverItems = items
          this.totalItems = total
          this.loading = false
        })
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop row selection

Example code

```vue
<template>
  <v-data-table
    v-model="selected"
    :items="items"
    item-value="name"
    show-select
  ></v-data-table>
</template>

<script setup>
  import { ref } from 'vue'

  const selected = ref([])
  const items = [
    {
      name: '🍎 Apple',
      location: 'Washington',
      height: '0.1',
      base: '0.07',
      volume: '0.0001',
    },
    {
      name: '🍌 Banana',
      location: 'Ecuador',
      height: '0.2',
      base: '0.05',
      volume: '0.0002',
    },
    {
      name: '🍇 Grapes',
      location: 'Italy',
      height: '0.02',
      base: '0.02',
      volume: '0.00001',
    },
    {
      name: '🍉 Watermelon',
      location: 'China',
      height: '0.4',
      base: '0.3',
      volume: '0.03',
    },
    {
      name: '🍍 Pineapple',
      location: 'Thailand',
      height: '0.3',
      base: '0.2',
      volume: '0.005',
    },
    {
      name: '🍒 Cherries',
      location: 'Turkey',
      height: '0.02',
      base: '0.02',
      volume: '0.00001',
    },
    {
      name: '🥭 Mango',
      location: 'India',
      height: '0.15',
      base: '0.1',
      volume: '0.0005',
    },
    {
      name: '🍓 Strawberry',
      location: 'USA',
      height: '0.03',
      base: '0.03',
      volume: '0.00002',
    },
    {
      name: '🍑 Peach',
      location: 'China',
      height: '0.09',
      base: '0.08',
      volume: '0.0004',
    },
    {
      name: '🥝 Kiwi',
      location: 'New Zealand',
      height: '0.05',
      base: '0.05',
      volume: '0.0001',
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        selected: [],
        items: [
          {
            name: '🍎 Apple',
            location: 'Washington',
            height: '0.1',
            base: '0.07',
            volume: '0.0001',
          },
          {
            name: '🍌 Banana',
            location: 'Ecuador',
            height: '0.2',
            base: '0.05',
            volume: '0.0002',
          },
          {
            name: '🍇 Grapes',
            location: 'Italy',
            height: '0.02',
            base: '0.02',
            volume: '0.00001',
          },
          {
            name: '🍉 Watermelon',
            location: 'China',
            height: '0.4',
            base: '0.3',
            volume: '0.03',
          },
          {
            name: '🍍 Pineapple',
            location: 'Thailand',
            height: '0.3',
            base: '0.2',
            volume: '0.005',
          },
          {
            name: '🍒 Cherries',
            location: 'Turkey',
            height: '0.02',
            base: '0.02',
            volume: '0.00001',
          },
          {
            name: '🥭 Mango',
            location: 'India',
            height: '0.15',
            base: '0.1',
            volume: '0.0005',
          },
          {
            name: '🍓 Strawberry',
            location: 'USA',
            height: '0.03',
            base: '0.03',
            volume: '0.00002',
          },
          {
            name: '🍑 Peach',
            location: 'China',
            height: '0.09',
            base: '0.08',
            volume: '0.0004',
          },
          {
            name: '🥝 Kiwi',
            location: 'New Zealand',
            height: '0.05',
            base: '0.05',
            volume: '0.0001',
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - misc expand

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="movies"
    item-value="title"
    hide-default-footer
    show-expand
  >
    <template v-slot:item.data-table-expand="{ internalItem, isExpanded, toggleExpand }">
      <v-btn
        :append-icon="isExpanded(internalItem) ? 'mdi-chevron-up' : 'mdi-chevron-down'"
        :text="isExpanded(internalItem) ? 'Collapse' : 'More info'"
        class="text-none"
        color="medium-emphasis"
        size="small"
        variant="text"
        border
        slim
        @click="toggleExpand(internalItem)"
      ></v-btn>
    </template>

    <template v-slot:expanded-row="{ columns, item }">
      <tr>
        <td :colspan="columns.length" class="py-2">
          <v-sheet rounded="lg" border>
            <v-table density="compact">
              <tbody class="bg-surface-light">
                <tr>
                  <th>Rating</th>
                  <th>Synopsis</th>
                  <th>Cast</th>
                </tr>
              </tbody>

              <tbody>
                <tr>
                  <td>
                    <v-rating
                      :model-value="item.details.rating"
                      color="orange-darken-2"
                      density="comfortable"
                      size="x-small"
                      half-increments
                      readonly
                    ></v-rating>
                  </td>
                  <td>{{ item.details.synopsis }}</td>
                  <td>{{ item.details.cast.join(', ') }}</td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>

<script setup>
  const headers = [
    { title: 'Title', key: 'title', align: 'start', sortable: true },
    { title: 'Director', key: 'director' },
    { title: 'Genre', key: 'genre' },
    { title: 'Year', key: 'year', align: 'end' },
    { title: 'Runtime(min)', key: 'runtime', align: 'end' },
  ]

  const movies = [
    {
      title: 'The Shawshank Redemption',
      director: 'Frank Darabont',
      genre: 'Drama',
      year: 1994,
      runtime: 142,
      details: {
        synopsis: 'Two imprisoned men bond over years, finding solace and redemption through acts of decency.',
        cast: ['Tim Robbins', 'Morgan Freeman'],
        rating: 3.5,
      },
    },
    {
      title: 'Inception',
      director: 'Christopher Nolan',
      genre: 'Sci-Fi',
      year: 2010,
      runtime: 148,
      details: {
        synopsis: 'A thief with the ability to enter dreams is tasked with stealing a secret from the subconscious.',
        cast: ['Leonardo DiCaprio', 'Joseph Gordon-Levitt'],
        rating: 5,
      },
    },
    {
      title: 'The Godfather',
      director: 'Francis Ford Coppola',
      genre: 'Crime',
      year: 1972,
      runtime: 175,
      details: {
        synopsis: 'The aging patriarch of a crime dynasty transfers control to his reluctant son.',
        cast: ['Marlon Brando', 'Al Pacino'],
        rating: 4.5,
      },
    },
    {
      title: 'Pulp Fiction',
      director: 'Quentin Tarantino',
      genre: 'Crime',
      year: 1994,
      runtime: 154,
      details: {
        synopsis: 'Interwoven stories of criminals, violence, and redemption in Los Angeles.',
        cast: ['John Travolta', 'Samuel L. Jackson'],
        rating: 4.5,
      },
    },
    {
      title: 'The Dark Knight',
      director: 'Christopher Nolan',
      genre: 'Action',
      year: 2008,
      runtime: 152,
      details: {
        synopsis: 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
        cast: ['Christian Bale', 'Heath Ledger'],
        rating: 4,
      },
    },
  ]
</script>

```

# Vuetify component v-data-table - virtual

Example code

```vue
<template>
  <v-data-table-virtual
    :headers="headers"
    :items="virtualBoats"
    height="400"
    item-value="name"
    fixed-header
  ></v-data-table-virtual>
</template>

<script setup>
  import { computed } from 'vue'

  const headers = [
    { title: 'Boat Type', align: 'start', key: 'name' },
    { title: 'Speed(knots)', align: 'end', key: 'speed' },
    { title: 'Length(m)', align: 'end', key: 'length' },
    { title: 'Price($)', align: 'end', key: 'price', value: item => formatPrice(item.price) },
    { title: 'Year', align: 'end', key: 'year' },
  ]

  const boats = [
    {
      name: 'Speedster',
      speed: 35,
      length: 22,
      price: 300000,
      year: 2021,
    },
    {
      name: 'OceanMaster',
      speed: 25,
      length: 35,
      price: 500000,
      year: 2020,
    },
    {
      name: 'Voyager',
      speed: 20,
      length: 45,
      price: 700000,
      year: 2019,
    },
    {
      name: 'WaveRunner',
      speed: 40,
      length: 19,
      price: 250000,
      year: 2022,
    },
    {
      name: 'SeaBreeze',
      speed: 28,
      length: 31,
      price: 450000,
      year: 2018,
    },
    {
      name: 'HarborGuard',
      speed: 18,
      length: 50,
      price: 800000,
      year: 2017,
    },
    {
      name: 'SlickFin',
      speed: 33,
      length: 24,
      price: 350000,
      year: 2021,
    },
    {
      name: 'StormBreaker',
      speed: 22,
      length: 38,
      price: 600000,
      year: 2020,
    },
    {
      name: 'WindSail',
      speed: 15,
      length: 55,
      price: 900000,
      year: 2019,
    },
    {
      name: 'FastTide',
      speed: 37,
      length: 20,
      price: 280000,
      year: 2022,
    },
  ]

  const virtualBoats = computed(() => {
    return [...Array(10000).keys()].map(i => {
      const boat = { ...boats[i % 10] }
      boat.name = `${boat.name} #${i}`
      return boat
    })
  })

  function formatPrice (value) {
    return `$${value.toFixed(0).replace(/\d(?=(\d{3})+$)/g, '$&,')}`
  }
</script>

<script>
  export default {
    data () {
      return {
        headers: [
          { title: 'Boat Type', align: 'start', key: 'name' },
          { title: 'Speed(knots)', align: 'end', key: 'speed' },
          { title: 'Length(m)', align: 'end', key: 'length' },
          { title: 'Price($)', align: 'end', key: 'price', value: item => formatPrice(item.price) },
          { title: 'Year', align: 'end', key: 'year' },
        ],
        boats: [
          {
            name: 'Speedster',
            speed: 35,
            length: 22,
            price: 300000,
            year: 2021,
          },
          {
            name: 'OceanMaster',
            speed: 25,
            length: 35,
            price: 500000,
            year: 2020,
          },
          {
            name: 'Voyager',
            speed: 20,
            length: 45,
            price: 700000,
            year: 2019,
          },
          {
            name: 'WaveRunner',
            speed: 40,
            length: 19,
            price: 250000,
            year: 2022,
          },
          {
            name: 'SeaBreeze',
            speed: 28,
            length: 31,
            price: 450000,
            year: 2018,
          },
          {
            name: 'HarborGuard',
            speed: 18,
            length: 50,
            price: 800000,
            year: 2017,
          },
          {
            name: 'SlickFin',
            speed: 33,
            length: 24,
            price: 350000,
            year: 2021,
          },
          {
            name: 'StormBreaker',
            speed: 22,
            length: 38,
            price: 600000,
            year: 2020,
          },
          {
            name: 'WindSail',
            speed: 15,
            length: 55,
            price: 900000,
            year: 2019,
          },
          {
            name: 'FastTide',
            speed: 37,
            length: 20,
            price: 280000,
            year: 2022,
          },
        ],
      }
    },

    computed: {
      virtualBoats () {
        return [...Array(10000).keys()].map(i => {
          const boat = { ...this.boats[i % this.boats.length] }
          boat.name = `${boat.name} #${i}`
          return boat
        })
      },
    },

    methods: {
      formatPrice (value) {
        return `$${value.toFixed(0).replace(/\d(?=(\d{3})+$)/g, '$&,')}`
      },
    },
  }
</script>

```

# Vuetify component v-data-table - slot header

Example code

```vue
<template>
  <v-data-table :items="items">
    <template v-slot:header.id="{ column }">
      {{ column.title.toUpperCase() }}
    </template>
  </v-data-table>
</template>

<script setup>
  const items = [
    {
      id: 1,
      name: 'T-Shirt',
      size: 'M',
      color: 'Red',
      price: 19.99,
      quantity: 10,
    },
    {
      id: 2,
      name: 'Jeans',
      size: '32',
      color: 'Blue',
      price: 49.99,
      quantity: 5,
    },
    {
      id: 3,
      name: 'Sweater',
      size: 'L',
      color: 'Green',
      price: 29.99,
      quantity: 7,
    },
    {
      id: 4,
      name: 'Jacket',
      size: 'XL',
      color: 'Black',
      price: 89.99,
      quantity: 3,
    },
    {
      id: 5,
      name: 'Socks',
      size: 'One Size',
      color: 'White',
      price: 9.99,
      quantity: 20,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          name: 'T-Shirt',
          size: 'M',
          color: 'Red',
          price: 19.99,
          quantity: 10,
        },
        {
          id: 2,
          name: 'Jeans',
          size: '32',
          color: 'Blue',
          price: 49.99,
          quantity: 5,
        },
        {
          id: 3,
          name: 'Sweater',
          size: 'L',
          color: 'Green',
          price: 29.99,
          quantity: 7,
        },
        {
          id: 4,
          name: 'Jacket',
          size: 'XL',
          color: 'Black',
          price: 89.99,
          quantity: 3,
        },
        {
          id: 5,
          name: 'Socks',
          size: 'One Size',
          color: 'White',
          price: 9.99,
          quantity: 20,
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - slot simple checkbox

Example code

```vue
<template>
  <v-data-table :items="consoles" hide-default-footer>
    <template v-slot:item.exclusive="{ item }">
      <v-checkbox-btn
        v-model="item.exclusive"
        :ripple="false"
      ></v-checkbox-btn>
    </template>
  </v-data-table>
</template>

<script setup>
  import { ref } from 'vue'

  const consoles = ref([
    {
      name: 'PlayStation 5',
      manufacturer: 'Sony',
      year: 2020,
      sales: '10M',
      exclusive: true,
    },
    {
      name: 'Xbox Series X',
      manufacturer: 'Microsoft',
      year: 2020,
      sales: '6.5M',
      exclusive: false,
    },
    {
      name: 'Nintendo Switch',
      manufacturer: 'Nintendo',
      year: 2017,
      sales: '89M',
      exclusive: true,
    },
    {
      name: 'PlayStation 4',
      manufacturer: 'Sony',
      year: 2013,
      sales: '116M',
      exclusive: true,
    },
    {
      name: 'Xbox One',
      manufacturer: 'Microsoft',
      year: 2013,
      sales: '50M',
      exclusive: false,
    },
    {
      name: 'Nintendo Wii',
      manufacturer: 'Nintendo',
      year: 2006,
      sales: '101M',
      exclusive: true,
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      consoles: [
        {
          name: 'PlayStation 5',
          manufacturer: 'Sony',
          year: 2020,
          sales: '10M',
          exclusive: true,
        },
        {
          name: 'Xbox Series X',
          manufacturer: 'Microsoft',
          year: 2020,
          sales: '6.5M',
          exclusive: false,
        },
        {
          name: 'Nintendo Switch',
          manufacturer: 'Nintendo',
          year: 2017,
          sales: '89M',
          exclusive: true,
        },
        {
          name: 'PlayStation 4',
          manufacturer: 'Sony',
          year: 2013,
          sales: '116M',
          exclusive: true,
        },
        {
          name: 'Xbox One',
          manufacturer: 'Microsoft',
          year: 2013,
          sales: '50M',
          exclusive: false,
        },
        {
          name: 'Nintendo Wii',
          manufacturer: 'Nintendo',
          year: 2006,
          sales: '101M',
          exclusive: true,
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - slot item

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="employees"
    class="text-caption"
    density="compact"
    item-value="name"
    hide-default-footer
    hover
  >
    <template v-slot:item="{ item }">
      <tr class="text-no-wrap">
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.department }}</td>
        <td>{{ item.role }}</td>
        <td
          :class="{
            'text-end': true,
            'bg-success': item.salary > 80000,
            'bg-warning': item.salary > 70000 && item.salary <= 80000,
            'bg-error': item.salary <= 70000
          }"
          v-text="`$${item.salary.toLocaleString()}`"
        ></td>
        <td>{{ item.hireDate }}</td>
        <td class="text-end">{{ item.hoursPerWeek }}</td>
        <td>{{ item.location }}</td>
        <td>{{ item.status }}</td>
        <td class="text-end">
          <v-chip
            :text="item.score.toFixed(2)"
            append-icon="mdi-open-in-new"
            size="x-small"
            @click=""
          ></v-chip>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>

<script setup>
  const headers = [
    { title: 'ID', key: 'id', align: 'start' },
    { title: 'Name', key: 'name' },
    { title: 'Dept', key: 'department' },
    { title: 'Role', key: 'role' },
    { title: 'Salary($)', key: 'salary', align: 'end' },
    { title: 'HireDate', key: 'hireDate' },
    { title: 'Hours/Wk', key: 'hoursPerWeek', align: 'end' },
    { title: 'Location', key: 'location' },
    { title: 'Status', key: 'status' },
    { title: 'Score', key: 'score', align: 'end' },
  ]
  const employees = [
    {
      id: 'E001',
      name: 'Alice Johnson',
      department: 'Engineering',
      role: 'Software Dev',
      salary: 95000,
      hireDate: '2020-03-15',
      hoursPerWeek: 40,
      location: 'New York',
      status: 'Full-Time',
      score: 4.5,
    },
    {
      id: 'E002',
      name: 'Bob Carter',
      department: 'Sales',
      role: 'Account Manager',
      salary: 72000,
      hireDate: '2019-11-01',
      hoursPerWeek: 35,
      location: 'Chicago',
      status: 'Full-Time',
      score: 4.2,
    },
    {
      id: 'E003',
      name: 'Clara Diaz',
      department: 'HR',
      role: 'Recruiter',
      salary: 65000,
      hireDate: '2021-06-10',
      hoursPerWeek: 32,
      location: 'Remote',
      status: 'Part-Time',
      score: 4.0,
    },
    {
      id: 'E004',
      name: 'David Lee',
      department: 'Engineering',
      role: 'DevOps Engineer',
      salary: 105000,
      hireDate: '2018-09-22',
      hoursPerWeek: 40,
      location: 'San Francisco',
      status: 'Full-Time',
      score: 4.7,
    },
    {
      id: 'E005',
      name: 'Ella Smith',
      department: 'Marketing',
      role: 'Social Media Mgr',
      salary: 80000,
      hireDate: '2020-01-05',
      hoursPerWeek: 38,
      location: 'Los Angeles',
      status: 'Full-Time',
      score: 4.3,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      headers: [
        { title: 'ID', key: 'id', align: 'start' },
        { title: 'Name', key: 'name' },
        { title: 'Dept', key: 'department' },
        { title: 'Role', key: 'role' },
        { title: 'Salary($)', key: 'salary', align: 'end' },
        { title: 'HireDate', key: 'hireDate' },
        { title: 'Hours/Wk', key: 'hoursPerWeek', align: 'end' },
        { title: 'Location', key: 'location' },
        { title: 'Status', key: 'status' },
        { title: 'Score', key: 'score', align: 'end' },
      ],
      employees: [
        {
          id: 'E001',
          name: 'Alice Johnson',
          department: 'Engineering',
          role: 'Software Dev',
          salary: 95000,
          hireDate: '2020-03-15',
          hoursPerWeek: 40,
          location: 'New York',
          status: 'Full-Time',
          score: 4.5,
        },
        {
          id: 'E002',
          name: 'Bob Carter',
          department: 'Sales',
          role: 'Account Manager',
          salary: 72000,
          hireDate: '2019-11-01',
          hoursPerWeek: 35,
          location: 'Chicago',
          status: 'Full-Time',
          score: 4.2,
        },
        {
          id: 'E003',
          name: 'Clara Diaz',
          department: 'HR',
          role: 'Recruiter',
          salary: 65000,
          hireDate: '2021-06-10',
          hoursPerWeek: 32,
          location: 'Remote',
          status: 'Part-Time',
          score: 4.0,
        },
        {
          id: 'E004',
          name: 'David Lee',
          department: 'Engineering',
          role: 'DevOps Engineer',
          salary: 105000,
          hireDate: '2018-09-22',
          hoursPerWeek: 40,
          location: 'San Francisco',
          status: 'Full-Time',
          score: 4.7,
        },
        {
          id: 'E005',
          name: 'Ella Smith',
          department: 'Marketing',
          role: 'Social Media Mgr',
          salary: 80000,
          hireDate: '2020-01-05',
          hoursPerWeek: 38,
          location: 'Los Angeles',
          status: 'Full-Time',
          score: 4.3,
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - prop item selectable

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    item-selectable="selectable"
    item-value="name"
    items-per-page="5"
    show-select
  ></v-data-table>
</template>

<script setup>
  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      key: 'name',
    },
    { title: 'Calories', align: 'end', key: 'calories' },
    { title: 'Fat (g)', align: 'end', key: 'fat' },
    { title: 'Carbs (g)', align: 'end', key: 'carbs' },
    { title: 'Protein (g)', align: 'end', key: 'protein' },
    { title: 'Iron (%)', align: 'end', key: 'iron' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
      selectable: false,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
      selectable: true,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
      selectable: true,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
      selectable: false,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
      selectable: true,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
      selectable: true,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
      selectable: true,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
      selectable: false,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
      selectable: true,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
      selectable: true,
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            title: 'Dessert (100g serving)',
            align: 'start',
            key: 'name',
          },
          { title: 'Calories', align: 'end', key: 'calories' },
          { title: 'Fat (g)', align: 'end', key: 'fat' },
          { title: 'Carbs (g)', align: 'end', key: 'carbs' },
          { title: 'Protein (g)', align: 'end', key: 'protein' },
          { title: 'Iron (%)', align: 'end', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
            selectable: false,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
            selectable: true,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
            selectable: true,
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
            selectable: false,
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
            selectable: true,
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
            selectable: true,
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
            selectable: true,
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
            selectable: false,
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
            selectable: true,
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
            selectable: true,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - prop multi sort

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    :sort-by="[{ key: 'calories', order: 'asc' }, { key: 'fat', order: 'desc' }]"
    multi-sort
  ></v-data-table>
</template>

<script setup>
  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Calories', key: 'calories' },
    { title: 'Fat (g)', key: 'fat' },
    { title: 'Carbs (g)', key: 'carbs' },
    { title: 'Protein (g)', key: 'protein' },
    { title: 'Iron (%)', key: 'iron' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 200,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 200,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 300,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 300,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 400,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 400,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 400,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 400,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 500,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 500,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            title: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            key: 'name',
          },
          { title: 'Calories', key: 'calories' },
          { title: 'Fat (g)', key: 'fat' },
          { title: 'Carbs (g)', key: 'carbs' },
          { title: 'Protein (g)', key: 'protein' },
          { title: 'Iron (%)', key: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 200,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 200,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          },
          {
            name: 'Eclair',
            calories: 300,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: 7,
          },
          {
            name: 'Cupcake',
            calories: 300,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: 8,
          },
          {
            name: 'Gingerbread',
            calories: 400,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: 16,
          },
          {
            name: 'Jelly bean',
            calories: 400,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: 0,
          },
          {
            name: 'Lollipop',
            calories: 400,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: 2,
          },
          {
            name: 'Honeycomb',
            calories: 400,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: 45,
          },
          {
            name: 'Donut',
            calories: 500,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: 22,
          },
          {
            name: 'KitKat',
            calories: 500,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: 6,
          },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-data-table - prop footer props

Example code

```vue
<template>
  <v-data-table
    :footer-props="{
      showFirstLastPage: true,
      firstIcon: 'mdi-arrow-collapse-left',
      lastIcon: 'mdi-arrow-collapse-right',
      prevIcon: 'mdi-minus',
      nextIcon: 'mdi-plus'
    }"
    :headers="headers"
    :items="desserts"
    :items-per-page="5"
    item-key="name"
  ></v-data-table>
</template>

<script setup>
  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      value: 'name',
    },
    { title: 'Category', value: 'category' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      category: 'Ice cream',
    },
    {
      name: 'Ice cream sandwich',
      category: 'Ice cream',
    },
    {
      name: 'Eclair',
      category: 'Cookie',
    },
    {
      name: 'Cupcake',
      category: 'Pastry',
    },
    {
      name: 'Gingerbread',
      category: 'Cookie',
    },
    {
      name: 'Jelly bean',
      category: 'Candy',
    },
    {
      name: 'Lollipop',
      category: 'Candy',
    },
    {
      name: 'Honeycomb',
      category: 'Toffee',
    },
    {
      name: 'Donut',
      category: 'Pastry',
    },
    {
      name: 'KitKat',
      category: 'Candy',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      headers: [
        {
          title: 'Dessert (100g serving)',
          align: 'start',
          value: 'name',
        },
        { title: 'Category', value: 'category' },
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          category: 'Ice cream',
        },
        {
          name: 'Ice cream sandwich',
          category: 'Ice cream',
        },
        {
          name: 'Eclair',
          category: 'Cookie',
        },
        {
          name: 'Cupcake',
          category: 'Pastry',
        },
        {
          name: 'Gingerbread',
          category: 'Cookie',
        },
        {
          name: 'Jelly bean',
          category: 'Candy',
        },
        {
          name: 'Lollipop',
          category: 'Candy',
        },
        {
          name: 'Honeycomb',
          category: 'Toffee',
        },
        {
          name: 'Donut',
          category: 'Pastry',
        },
        {
          name: 'KitKat',
          category: 'Candy',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-data-table - virtualized

Example code

```vue
<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :items-per-page="-1"
    height="500"
    hide-default-footer
    virtual-rows
  ></v-data-table>
</template>

<script setup>
  import { computed } from 'vue'

  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6,
      carbs: 24,
      protein: 4,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16,
      carbs: 23,
      protein: 6,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0,
      carbs: 94,
      protein: 0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]
  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Calories', key: 'calories' },
    { title: 'Fat (g)', key: 'fat' },
    { title: 'Carbs (g)', key: 'carbs' },
    { title: 'Protein (g)', key: 'protein' },
    { title: 'Iron (%)', key: 'iron' },
  ]

  const items = computed(() => {
    return [...new Array(100)].reduce(items => {
      items.push(...desserts)
      return items
    }, [])
  })
</script>

<script>
  const desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159,
      fat: 6.0,
      carbs: 24,
      protein: 4.0,
      iron: 1,
    },
    {
      name: 'Ice cream sandwich',
      calories: 237,
      fat: 9.0,
      carbs: 37,
      protein: 4.3,
      iron: 1,
    },
    {
      name: 'Eclair',
      calories: 262,
      fat: 16.0,
      carbs: 23,
      protein: 6.0,
      iron: 7,
    },
    {
      name: 'Cupcake',
      calories: 305,
      fat: 3.7,
      carbs: 67,
      protein: 4.3,
      iron: 8,
    },
    {
      name: 'Gingerbread',
      calories: 356,
      fat: 16.0,
      carbs: 49,
      protein: 3.9,
      iron: 16,
    },
    {
      name: 'Jelly bean',
      calories: 375,
      fat: 0.0,
      carbs: 94,
      protein: 0.0,
      iron: 0,
    },
    {
      name: 'Lollipop',
      calories: 392,
      fat: 0.2,
      carbs: 98,
      protein: 0,
      iron: 2,
    },
    {
      name: 'Honeycomb',
      calories: 408,
      fat: 3.2,
      carbs: 87,
      protein: 6.5,
      iron: 45,
    },
    {
      name: 'Donut',
      calories: 452,
      fat: 25.0,
      carbs: 51,
      protein: 4.9,
      iron: 22,
    },
    {
      name: 'KitKat',
      calories: 518,
      fat: 26.0,
      carbs: 65,
      protein: 7,
      iron: 6,
    },
  ]

  export default {
    data: () => ({
      headers: [
        {
          title: 'Dessert (100g serving)',
          align: 'start',
          sortable: false,
          key: 'name',
        },
        { title: 'Calories', key: 'calories' },
        { title: 'Fat (g)', key: 'fat' },
        { title: 'Carbs (g)', key: 'carbs' },
        { title: 'Protein (g)', key: 'protein' },
        { title: 'Iron (%)', key: 'iron' },
      ],
    }),
    computed: {
      items () {
        return [...new Array(100)].reduce(items => {
          items.push(...desserts)
          return items
        }, [])
      },
    },
  }
</script>

```

# Vuetify component v-data-table - prop grouping

Example code

```vue
<template>
  <v-data-table
    :group-by="groupBy"
    :headers="headers"
    :items="desserts"
    :sort-by="sortBy"
    item-value="name"
  ></v-data-table>
</template>
<script setup>
  import { ref } from 'vue'

  const sortBy = ref([{ key: 'name', order: 'asc' }])
  const groupBy = ref([{ key: 'dairy', order: 'asc' }])

  const headers = [
    {
      title: 'Dessert (100g serving)',
      align: 'start',
      key: 'name',
      groupable: false,
    },
    { title: 'Category', key: 'category', align: 'end' },
    { title: 'Dairy', key: 'dairy', align: 'end' },
  ]
  const desserts = [
    {
      name: 'Frozen Yogurt',
      category: 'Ice cream',
      dairy: 'Yes',
    },
    {
      name: 'Ice cream sandwich',
      category: 'Ice cream',
      dairy: 'Yes',
    },
    {
      name: 'Eclair',
      category: 'Cookie',
      dairy: 'Yes',
    },
    {
      name: 'Cupcake',
      category: 'Pastry',
      dairy: 'Yes',
    },
    {
      name: 'Gingerbread',
      category: 'Cookie',
      dairy: 'No',
    },
    {
      name: 'Jelly bean',
      category: 'Candy',
      dairy: 'No',
    },
    {
      name: 'Lollipop',
      category: 'Candy',
      dairy: 'No',
    },
    {
      name: 'Honeycomb',
      category: 'Toffee',
      dairy: 'No',
    },
    {
      name: 'Donut',
      category: 'Pastry',
      dairy: 'Yes',
    },
    {
      name: 'KitKat',
      category: 'Candy',
      dairy: 'Yes',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      sortBy: [{ key: 'name', order: 'asc' }],
      groupBy: [{ key: 'dairy', order: 'asc' }],
      headers: [
        {
          title: 'Dessert (100g serving)',
          align: 'start',
          key: 'name',
          groupable: false,
        },
        { title: 'Category', key: 'category', align: 'end' },
        { title: 'Dairy', key: 'dairy', align: 'end' },
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          category: 'Ice cream',
          dairy: 'Yes',
        },
        {
          name: 'Ice cream sandwich',
          category: 'Ice cream',
          dairy: 'Yes',
        },
        {
          name: 'Eclair',
          category: 'Cookie',
          dairy: 'Yes',
        },
        {
          name: 'Cupcake',
          category: 'Pastry',
          dairy: 'Yes',
        },
        {
          name: 'Gingerbread',
          category: 'Cookie',
          dairy: 'No',
        },
        {
          name: 'Jelly bean',
          category: 'Candy',
          dairy: 'No',
        },
        {
          name: 'Lollipop',
          category: 'Candy',
          dairy: 'No',
        },
        {
          name: 'Honeycomb',
          category: 'Toffee',
          dairy: 'No',
        },
        {
          name: 'Donut',
          category: 'Pastry',
          dairy: 'Yes',
        },
        {
          name: 'KitKat',
          category: 'Candy',
          dairy: 'Yes',
        },
      ],
    }),
  }
</script>

```
