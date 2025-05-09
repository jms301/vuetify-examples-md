# Vuetify component v-sheet - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="py-8 bg-surface-bright">
      <v-sheet
        v-if="sheet"
        v-model="sheet"
        v-bind="props"
        class="mx-auto"
      >
        <template v-slot:text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </template>
      </v-sheet>

      <div class="text-center">
        <v-btn v-if="!sheet" @click="sheet = true">
          Show sheet
        </v-btn>
      </div>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="color"
        :items="[
          'success',
          'info',
          'warning',
          'error',
        ]"
        label="Color"
        clearable
      ></v-select>

      <v-checkbox v-model="border" label="Border"></v-checkbox>

      <v-checkbox v-model="rounded" label="Rounded"></v-checkbox>

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
  const name = 'v-sheet'
  const model = ref('default')
  const sheet = ref(true)
  const border = ref(false)
  const elevation = ref(0)
  const rounded = ref(false)
  const color = ref()
  const options = []
  const props = computed(() => {
    return {
      elevation: elevation.value || undefined,
      height: 200,
      width: 200,
      border: border.value || undefined,
      color: color.value || undefined,
      rounded: rounded.value || undefined,
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

# Vuetify component v-sheet - prop rounded

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col
        v-for="rounded in [false, true, 'xl']"
        :key="String(rounded)"
        cols="12"
        md="4"
      >
        <v-sheet
          class="pa-12"
          color="grey-lighten-3"
        >
          <div></div>
          <v-sheet
            :rounded="rounded"
            class="mx-auto"
            height="100"
            width="100"
          ></v-sheet>
          <div></div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-sheet - misc privacy policy

Example code

```vue
<template>
  <v-sheet
    border="md"
    class="pa-6 text-white mx-auto"
    color="#141518"
    max-width="400"
  >
    <h4 class="text-h5 font-weight-bold mb-4">Your Privacy</h4>

    <p class="mb-8">
      This business determines the use of personal data collected on our media properties and across the internet. We may collect data that you submit to us directly or data that we collect automatically including from cookies (such as device information or IP address).

      <br>
      <br>

      Please read our <a class="text-red-accent-2" href="#">Privacy Policy</a> to learn about our privacy practices or click "Your Preferences" to exercise control over your data.
    </p>

    <v-btn
      class="text-none text-black mb-4"
      color="red-accent-2"
      size="x-large"
      variant="flat"
      block
    >
      Accept
    </v-btn>

    <v-btn
      class="text-none text-black"
      color="red-accent-2"
      size="x-large"
      variant="outlined"
      block
    >
      Your Preferences
    </v-btn>
  </v-sheet>
</template>

```

# Vuetify component v-sheet - prop elevation

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col
        v-for="elevation in elevations"
        :key="elevation"
        cols="12"
        md="4"
      >
        <v-sheet
          class="pa-12"
          color="grey-lighten-3"
        >
          <v-sheet
            :elevation="elevation"
            class="mx-auto"
            height="100"
            width="100"
          ></v-sheet>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  const elevations = [0, 4, 8, 12, 16, 20]
</script>

<script>
  export default {
    data: () => ({
      elevations: [0, 4, 8, 12, 16, 20],
    }),
  }
</script>

```

# Vuetify component v-sheet - misc referral program

Example code

```vue
<template>
  <v-sheet
    border="lg opacity-12"
    class="text-body-2 mx-auto"
    max-width="550"
  >
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="3">
          <v-img height="88" src="https://cdn.vuetifyjs.com/docs/images/graphics/img-placeholder.png" cover></v-img>
        </v-col>

        <v-col cols="12" md="9">
          <p class="mb-4">
            This is part of our <a href="#">Most Comprehensive Guide to Referral Programs</a> > <a href="#">Do I Need A Referral Program?</a> section. You may enjoy other related articles:
          </p>

          <ul class="ps-4 mb-6">
            <li>
              <a href="#">5 Ways to See if Referral Programs Can Work for You</a>
            </li>
            <li>
              <a href="#">The 6 Key Benefits of Referral Marketing</a>
            </li>
            <li>
              <a href="#">Leading Indicators of Referral Program Success</a>
            </li>
            <li>
              <a href="#">Debunking the Top 5 Worst Referral Program Myths</a>
            </li>
          </ul>

          <v-btn
            class="text-none"
            color="info"
            rounded="0"
            variant="flat"
            block
          >
            <span class="hidden-sm-and-down">
              Explore our 38+ Referral Program Resources
            </span>

            <span class="hidden-md-and-up">
              Explore Referral Resources
            </span>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-sheet>
</template>

```

# Vuetify component v-sheet - misc reconcile

Example code

```vue
<template>
  <v-sheet
    class="pa-4 text-center mx-auto"
    elevation="12"
    max-width="600"
    rounded="lg"
    width="100%"
  >
    <v-icon
      class="mb-5"
      color="success"
      icon="mdi-check-circle"
      size="112"
    ></v-icon>

    <h2 class="text-h5 mb-6">You reconciled this account</h2>

    <p class="mb-4 text-medium-emphasis text-body-2">
      To see a report on this reconciliation, click <a class="text-decoration-none text-info" href="#">View reconciliation report.</a>

      <br>

      Otherwise, you're done!
    </p>

    <v-divider class="mb-4"></v-divider>

    <div class="text-end">
      <v-btn
        class="text-none"
        color="success"
        variant="flat"
        width="90"
        rounded
      >
        Done
      </v-btn>
    </div>
  </v-sheet>
</template>

```

# Vuetify component v-sheet - prop color

Example code

```vue
<template>
  <v-container>
    <v-row class="flex-child text-subtitle-2">
      <v-col
        class="d-flex"
        cols="12"
        md="4"
      >
        <v-sheet
          class="d-flex"
          color="grey-lighten-3"
          height="424"
        >
          <sheet-footer>
            #1: (3r x 2c)
          </sheet-footer>
        </v-sheet>
      </v-col>

      <v-col
        class="d-flex"
        cols="12"
        md="4"
      >
        <v-row class="ma-n3">
          <v-col cols="6">
            <v-sheet
              class="d-flex"
              color="green-lighten-3"
              height="150"
            >
              <sheet-footer>
                #2: (1r x 1c)
              </sheet-footer>
            </v-sheet>
          </v-col>

          <v-col cols="6">
            <v-sheet
              class="d-flex"
              color="yellow-lighten-3"
              height="150"
            >
              <sheet-footer>
                #3: (1r x 1c)
              </sheet-footer>
            </v-sheet>
          </v-col>

          <v-col cols="12">
            <v-sheet
              class="d-flex"
              color="red-lighten-3"
              height="250"
            >
              <sheet-footer>
                #5: (2r x 2c)
              </sheet-footer>
            </v-sheet>
          </v-col>
        </v-row>
      </v-col>

      <v-col
        cols="6"
        md="2"
      >
        <v-sheet
          class="d-flex"
          color="teal-lighten-3"
          height="300"
        >
          <sheet-footer>
            #4: (2r x 1c)
          </sheet-footer>
        </v-sheet>
      </v-col>

      <v-col
        class="d-flex"
        cols="6"
        md="2"
      >
        <v-sheet
          class="d-flex mt-auto"
          color="purple-lighten-3"
          height="300"
        >
          <sheet-footer>
            #6: (2r x 1c)
          </sheet-footer>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { h } from 'vue'

  const SheetFooter = {
    setup (_, { slots }) {
      return () => h('v-sheet', {
        class: 'ma-auto px-4',
        color: 'rgba(0, 0, 0, .36)',
        height: 50,
      }, slots.default())
    },
  }
</script>

<script>
  import { h } from 'vue'

  export default {
    components: {
      // A simple helper component
      SheetFooter: {
        setup (_, { slots }) {
          return () => h('v-sheet', {
            class: 'ma-auto px-4',
            color: 'rgba(0, 0, 0, .36)',
            height: 50,
          }, slots.default())
        },
      },
    },
  }
</script>

```

# Vuetify component v-sheet - misc congratulations

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-center justify-center flex-wrap text-center mx-auto px-4"
    elevation="4"
    height="250"
    max-width="800"
    width="100%"
    rounded
  >
    <div>
      <h2 class="text-h4 font-weight-black text-orange">Congratulations!</h2>

      <div class="text-h5 font-weight-medium mb-2">
        You are officially a part of the Vuetify Community!
      </div>

      <p class="text-body-2 mb-4">
        Please head over to your inbox/spam or others folder to find our verification email.
      </p>

      <v-btn color="orange" variant="text">Go to Login</v-btn>
    </div>
  </v-sheet>
</template>

```
