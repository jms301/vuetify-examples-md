# Vuetify concept spacing - usage

Example code

```vue
<template>
  <v-container
    class="spacing-playground pa-6"
    fluid
  >
    <v-row>
      <v-col
        class="d-flex align-center"
        cols="12"
        sm="6"
      >
        <v-select
          v-model="paddingDirection"
          :items="directions"
          class="pe-2"
          label="Padding"
        >
          <template v-slot:prepend>
            <strong class="text-primary py-1">p</strong>
          </template>

          <template v-slot:append-outer>
            <div class="py-1">
              -
            </div>
          </template>
        </v-select>

        <v-select
          v-model="paddingSize"
          :items="paddingSizes.slice(1)"
          label="Size"
        ></v-select>
      </v-col>

      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-select
          v-model="marginDirection"
          :items="directions"
          class="pe-2"
          label="Margin"
        >
          <template v-slot:prepend>
            <strong class="text-primary py-1">m</strong>
          </template>

          <template v-slot:append-outer>
            <div class="py-1">
              -
            </div>
          </template>
        </v-select>

        <v-select
          v-model="marginSize"
          :items="marginSizes"
          label="Size"
        ></v-select>
      </v-col>

      <v-col
        class="bg-orange-lighten-3 pa-0"
        cols="12"
      >
        <v-sheet
          :class="[computedMargin]"
          elevation="4"
          rounded
        >
          <div
            :class="[computedPadding]"
            class="bg-light-green-lighten-3"
          >
            <div
              class="bg-white text-center py-6"
              v-text="playgroundText"
            ></div>
          </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data () {
      const spacers = Array.from({ length: 17 }, (val, i) => `${i}`)
      const nspacers = Array.from({ length: 16 }, (val, i) => `n${i + 1}`)
      const defaults = ['auto', ...spacers]

      return {
        directions: ['t', 'b', 'l', 'r', 's', 'e', 'x', 'y', 'a'],
        marginDirection: 'a',
        marginSize: '2',
        marginSizes: [...defaults, ...nspacers],
        paddingDirection: 'a',
        paddingSize: '6',
        paddingSizes: defaults,
        playgroundText: 'Use the controls above to try out the different spacing helpers.',
      }
    },

    computed: {
      computedPadding () {
        return `p${this.paddingDirection}-${this.paddingSize}`
      },
      computedMargin () {
        return `m${this.marginDirection}-${this.marginSize}`
      },
    },
  }
</script>

```

# Vuetify concept spacing - gap

Example code

```vue
<template>
  <div class="d-flex flex-wrap ga-3">
    <v-card
      v-for="n in 8"
      :key="n"
      color="secondary"
      width="200px"
    >
      <v-card-text>
        Gapped
      </v-card-text>
    </v-card>
  </div>
</template>

```

# Vuetify concept spacing - horizontal

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="secondary"
    width="200px"
  >
    <v-card-text>
      Centered
    </v-card-text>
  </v-card>
</template>

```

# Vuetify concept spacing - negative margin

Example code

```vue
<template>
  <div>
    <v-card
      class="mx-auto"
      color="secondary"
      height="100"
      max-width="200"
    ></v-card>
    <v-card
      class="mt-n12 mx-auto"
      color="secondary"
      elevation="12"
      height="200"
      max-width="300"
    >
      <v-card-text>This card has negative top margin applied</v-card-text>
    </v-card>
  </div>
</template>

```

# Vuetify concept spacing - breakpoints

Example code

```vue
<template>
  <v-card
    class="pa-md-4 mx-lg-auto"
    color="secondary"
    width="250px"
  >
    <v-card-text>
      Adjust screen size to see spacing changes
    </v-card-text>
  </v-card>
</template>

```
