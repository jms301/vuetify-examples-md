# Vuetify component v-expansion-panels - usage

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
      <v-expansion-panels v-bind="props">
        <v-expansion-panel
          text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima"
          title="Title"
        >
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-expansion-panels'
  const model = ref('default')
  const options = []
  const props = computed(() => {
    return {}
  })

  const slots = computed(() => {
    return `
  <v-expansion-panel
    title="Title"
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima"
  >
  </v-expansion-panel>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-expansion-panels - prop variant

Example code

```vue
<template>
  <div>
    <div class="text-subtitle-2 mb-2">Default</div>
    <v-expansion-panels>
      <v-expansion-panel
        v-for="i in 3"
        :key="i"
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Item"
      ></v-expansion-panel>
    </v-expansion-panels>

    <div class="text-subtitle-2 mt-4 mb-2">Accordion</div>

    <v-expansion-panels variant="accordion">
      <v-expansion-panel
        v-for="i in 3"
        :key="i"
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Item"
      ></v-expansion-panel>
    </v-expansion-panels>

    <div class="text-subtitle-2 mt-4 mb-2">Inset</div>

    <v-expansion-panels class="my-4" variant="inset">
      <v-expansion-panel
        v-for="i in 3"
        :key="i"
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Item"
      ></v-expansion-panel>
    </v-expansion-panels>

    <div class="text-subtitle-2 mt-4 mb-2">Popout</div>

    <v-expansion-panels class="my-4" variant="popout">
      <v-expansion-panel
        v-for="i in 3"
        :key="i"
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Item"
      ></v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

```

# Vuetify component v-expansion-panels - prop readonly

Example code

```vue
<template>
  <div>
    <div class="d-flex">
      <v-checkbox
        v-model="readonly"
        label="Readonly"
      ></v-checkbox>
    </div>

    <v-expansion-panels
      v-model="panel"
      :readonly="readonly"
      multiple
    >
      <v-expansion-panel>
        <v-expansion-panel-title>Panel 1</v-expansion-panel-title>
        <v-expansion-panel-text>
          Some content
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>Panel 2</v-expansion-panel-title>
        <v-expansion-panel-text>
          Some content
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>Panel 3</v-expansion-panel-title>
        <v-expansion-panel-text>
          Some content
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const panel = ref([0, 1])
  const readonly = ref(false)
</script>

<script>
  export default {
    data: () => ({
      panel: [0, 1],
      readonly: false,
    }),
  }
</script>

```

# Vuetify component v-expansion-panels - misc custom icons

Example code

```vue
<template>
  <div>
    <v-expansion-panels class="mb-6">
      <v-expansion-panel
        v-for="i in 3"
        :key="i"
      >
        <v-expansion-panel-title expand-icon="mdi-menu-down">
          Item
        </v-expansion-panel-title>
        <v-expansion-panel-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-title collapse-icon="mdi-minus" expand-icon="mdi-plus">
          Item
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>
          Item
          <template v-slot:actions="{ expanded }">
            <v-icon :color="!expanded ? 'teal' : ''" :icon="expanded ? 'mdi-pencil' : 'mdi-check'"></v-icon>
          </template>
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title disable-icon-rotate>
          Item
          <template v-slot:actions>
            <v-icon color="error" icon="mdi-alert-circle">
            </v-icon>
          </template>
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

```

# Vuetify component v-expansion-panels - prop model

Example code

```vue
<template>
  <div>
    <div class="text-center d-flex pb-4">
      <v-btn class="ma-2" @click="all">
        All
      </v-btn>
      <v-btn class="ma-2" @click="none">
        None
      </v-btn>
    </div>

    <div class="pb-4">v-model {{ panel }}</div>

    <v-expansion-panels
      v-model="panel"
      multiple
    >
      <v-expansion-panel
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Foo"
        value="foo"
      ></v-expansion-panel>

      <v-expansion-panel
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Bar"
        value="bar"
      ></v-expansion-panel>

      <v-expansion-panel
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        title="Baz"
        value="baz"
      ></v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const panel = ref([])
  function all () {
    panel.value = ['foo', 'bar', 'baz']
  }
  function none () {
    panel.value = []
  }
</script>

<script>
  export default {
    data () {
      return {
        panel: [],
      }
    },
    methods: {
      all () {
        this.panel = ['foo', 'bar', 'baz']
      },
      none () {
        this.panel = []
      },
    },
  }
</script>

```

# Vuetify component v-expansion-panels - prop disabled

Example code

```vue
<template>
  <div>
    <div class="d-flex">
      <v-checkbox
        v-model="disabled"
        label="Disabled"
      ></v-checkbox>
    </div>

    <v-expansion-panels
      v-model="panel"
      :disabled="disabled"
      multiple
    >
      <v-expansion-panel>
        <v-expansion-panel-title>Panel 1</v-expansion-panel-title>
        <v-expansion-panel-text>
          Some content
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>Panel 2</v-expansion-panel-title>
        <v-expansion-panel-text>
          Some content
        </v-expansion-panel-text>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-title>Panel 3</v-expansion-panel-title>
        <v-expansion-panel-text>
          Some content
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const panel = ref([0, 1])
  const disabled = ref(false)
</script>

<script>
  export default {
    data: () => ({
      panel: [0, 1],
      disabled: false,
    }),
  }
</script>

```

# Vuetify component v-expansion-panels - misc advanced

Example code

```vue
<template>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-title>
        <template v-slot:default="{ expanded }">
          <v-row no-gutters>
            <v-col class="d-flex justify-start" cols="4">
              Trip name
            </v-col>
            <v-col
              class="text-grey"
              cols="8"
            >
              <v-fade-transition leave-absolute>
                <span
                  v-if="expanded"
                  key="0"
                >
                  Enter a name for the trip
                </span>
                <span
                  v-else
                  key="1"
                >
                  {{ trip.name }}
                </span>
              </v-fade-transition>
            </v-col>
          </v-row>
        </template>
      </v-expansion-panel-title>
      <v-expansion-panel-text>
        <v-text-field
          v-model="trip.name"
          placeholder="Caribbean Cruise"
          hide-details
        ></v-text-field>
      </v-expansion-panel-text>
    </v-expansion-panel>

    <v-expansion-panel>
      <v-expansion-panel-title v-slot="{ expanded }">
        <v-row no-gutters>
          <v-col class="d-flex justify-start" cols="4">
            Location
          </v-col>
          <v-col
            class="text--secondary"
            cols="8"
          >
            <v-fade-transition leave-absolute>
              <span
                v-if="expanded"
                key="0"
              >
                Select trip destination
              </span>
              <span
                v-else
                key="1"
              >
                {{ trip.location }}
              </span>
            </v-fade-transition>
          </v-col>
        </v-row>
      </v-expansion-panel-title>
      <v-expansion-panel-text>
        <v-row no-gutters>
          <v-spacer></v-spacer>
          <v-col cols="5">
            <v-select
              v-model="trip.location"
              :items="locations"
              variant="solo"
              chips
              flat
            ></v-select>
          </v-col>

          <v-divider
            class="mx-4"
            vertical
          ></v-divider>

          <v-col cols="3">
            Select your destination of choice
            <br>
            <a href="#">Learn more</a>
          </v-col>
        </v-row>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="secondary"
            variant="text"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            variant="text"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-expansion-panel-text>
    </v-expansion-panel>

    <v-expansion-panel>
      <v-expansion-panel-title v-slot="{ expanded }">
        <v-row no-gutters>
          <v-col class="d-flex justify-start" cols="4">
            Start and end dates
          </v-col>
          <v-col
            class="text--secondary"
            cols="8"
          >
            <v-fade-transition leave-absolute>
              <span v-if="expanded">When do you want to travel?</span>
              <v-row
                v-else
                style="width: 100%"
                no-gutters
              >
                <v-col class="d-flex justify-start" cols="6">
                  Start date: {{ trip.start || 'Not set' }}
                </v-col>
                <v-col class="d-flex justify-start" cols="6">
                  End date: {{ trip.end || 'Not set' }}
                </v-col>
              </v-row>
            </v-fade-transition>
          </v-col>
        </v-row>
      </v-expansion-panel-title>
      <v-expansion-panel-text>
        <v-row
          justify="space-around"
          no-gutters
        >
          <v-col cols="3">
            <v-text-field
              v-model="trip.start"
              label="Start date"
              type="date"
            ></v-text-field>
          </v-col>

          <v-col cols="3">
            <v-text-field
              v-model="trip.end"
              label="End date"
              type="date"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script setup>
  import { ref } from 'vue'

  const locations = ['Australia', 'Barbados', 'Chile', 'Denmark', 'Ecuador', 'France']

  const trip = ref({
    name: '',
    location: null,
    start: null,
    end: null,
  })
</script>

<script>
  export default {
    data: () => ({
      trip: {
        name: '',
        location: null,
        start: null,
        end: null,
      },
      locations: ['Australia', 'Barbados', 'Chile', 'Denmark', 'Ecuador', 'France'],
    }),
  }
</script>

```
