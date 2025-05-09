# Vuetify component v-skeleton-loader - usage

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
      <v-skeleton-loader
        v-bind="props"
        class="mx-auto"
        max-width="300"
      ></v-skeleton-loader>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="type"
        :items="types"
        label="Type"
        clearable
      ></v-select>

      <v-select
        v-model="color"
        :items="colors"
        label="Color"
        clearable
      ></v-select>

      <v-slider
        v-model="elevation"
        label="Elevation"
        max="24"
        min="0"
      ></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-skeleton-loader'
  const model = ref('default')
  const options = ['boilerplate']
  const elevation = ref()
  const color = ref()
  const colors = ['primary', 'secondary', 'success', 'info', 'warning', 'error']
  const type = ref('card')
  const types = ['card', 'paragraph', 'list-item-avatar', 'article', 'card-avatar']

  const props = computed(() => {
    return {
      elevation: elevation.value || undefined,
      boilerplate: model.value === 'boilerplate' || undefined,
      color: color.value || undefined,
      type: type.value || undefined,
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<v-skeleton-loader${propsToString(props.value)}>${slots.value}</v-skeleton-loader>`
  })
</script>

```

# Vuetify component v-skeleton-loader - prop boilerplate

Example code

```vue
<template>
  <v-skeleton-loader
    class="mx-auto"
    elevation="2"
    max-width="360"
    type="card-avatar, article, actions"
    boilerplate
  ></v-skeleton-loader>
</template>

```

# Vuetify component v-skeleton-loader - prop loading

Example code

```vue
<template>
  <v-container>
    <div class="text-center mb-12">
      <v-btn
        size="x-large"
        @click="loading = !loading"
      >
        Toggle Loading
      </v-btn>
    </div>

    <v-row justify="center">
      <v-col
        class="mb-12"
        cols="12"
        md="6"
      >
        <div class="text-h5 text-center">
          Using slot
        </div>

        <v-skeleton-loader
          :loading="loading"
          type="list-item-two-line"
        >
          <v-list-item
            lines="two"
            subtitle="Subtitle"
            title="Title"
            rounded
          ></v-list-item>
        </v-skeleton-loader>
      </v-col>

      <v-col
        cols="12"
        md="6"
      >
        <div class="text-h5 text-center">
          Using if
        </div>

        <v-skeleton-loader
          v-if="loading"
          type="list-item-two-line"
        ></v-skeleton-loader>

        <v-list-item
          v-else
          lines="two"
          subtitle="Subtitle"
          title="Title"
          rounded
        ></v-list-item>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const loading = ref(true)
</script>

<script>
  export default {
    data: () => ({
      loading: true,
    }),
  }
</script>

```

# Vuetify component v-skeleton-loader - prop elevation

Example code

```vue
<template>
  <v-skeleton-loader
    class="mx-auto"
    elevation="12"
    max-width="400"
    type="table-heading, list-item-two-line, image, table-tfoot"
  ></v-skeleton-loader>
</template>

```

# Vuetify component v-skeleton-loader - prop type

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6">
        <v-skeleton-loader
          class="mx-auto border"
          max-width="300"
          type="card-avatar, actions"
        ></v-skeleton-loader>
      </v-col>

      <v-col cols="12" md="6">
        <v-skeleton-loader
          class="mx-auto border"
          max-width="300"
          type="image, article"
        ></v-skeleton-loader>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-skeleton-loader - misc ice cream

Example code

```vue
<template>
  <div>
    <div class="text-center">
      <v-btn
        class="mb-12"
        size="x-large"
        @click="loading = !loading"
      >
        Toggle Loading
      </v-btn>
    </div>

    <v-card
      max-width="800"
      rounded="lg"
      theme="dark"
    >
      <v-container>
        <v-row>
          <v-col
            v-for="{ src, title, subtitle } in cards"
            :key="title"
            cols="12"
            lg="4"
            md="6"
          >
            <v-skeleton-loader
              :loading="loading"
              height="240"
              type="image, list-item-two-line"
            >
              <v-responsive>
                <v-img
                  :src="src"
                  class="rounded-lg mb-2"
                  height="184"
                  cover
                ></v-img>

                <v-list-item
                  :subtitle="subtitle"
                  :title="title"
                  class="px-0"
                ></v-list-item>
              </v-responsive>
            </v-skeleton-loader>
          </v-col>
        </v-row>

        <br>

        <v-chip
          prepend-icon="mdi-check-circle"
          size="large"
          variant="text"
          border
        >
          <template v-slot:prepend>
            <v-icon color="disabled"></v-icon>
          </template>

          <span class="text-subtitle-1">
            Homemade Dulce de Leche Ice Cream with Chocolate Chips
          </span>
        </v-chip>
      </v-container>
    </v-card>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const cards = [
    {
      title: 'Homemade Dulce de Leche Ice Cream with Chocolate Chips',
      subtitle: 'Happy Foods',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/dulce-ice-cream.png',
    },
    {
      title: 'Salted Caramel Swirl Ice Cream',
      subtitle: 'Stone Kitchen',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/salted-caramel-ice-cream.png',
    },
    {
      title: 'Peanut Butter No-Churn Ice Cream',
      subtitle: 'The Sweeter Side',
      src: 'https://cdn.vuetifyjs.com/docs/images/graphics/peanut-butter-ice-cream.png',
    },
  ]

  const loading = ref(true)
</script>

<script>
  export default {
    data: () => ({
      cards: [
        {
          title: 'Homemade Dulce de Leche Ice Cream with Chocolate Chips',
          subtitle: 'Happy Foods',
          src: 'https://cdn.vuetifyjs.com/docs/images/graphics/dulce-ice-cream.png',
        },
        {
          title: 'Salted Caramel Swirl Ice Cream',
          subtitle: 'Stone Kitchen',
          src: 'https://cdn.vuetifyjs.com/docs/images/graphics/salted-caramel-ice-cream.png',
        },
        {
          title: 'Peanut Butter No-Churn Ice Cream',
          subtitle: 'The Sweeter Side',
          src: 'https://cdn.vuetifyjs.com/docs/images/graphics/peanut-butter-ice-cream.png',
        },
      ],
      loading: true,
    }),
  }
</script>

```
