# Vuetify component v-stepper - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-stepper v-bind="props" v-model="step">
      <template v-slot:item.1>
        <v-card title="Step One" flat>
          <template v-slot:text>
            <div @blur="onBlur" @dblclick="onDblClick">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
            </div>
          </template>
        </v-card>
      </template>

      <template v-slot:item.2>
        <v-card title="Step Two" flat>
          <template v-slot:text>
            <div @blur="onBlur" @dblclick="onDblClick">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!
            </div>
          </template>
        </v-card>
      </template>

      <template v-slot:item.3>
        <v-card title="Step Three" flat>
          <template v-slot:text>
            <div @blur="onBlur" @dblclick="onDblClick">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!

              Lorem ipsum dolor sit amet consectetur adipisicing elit.
            </div>
          </template>
        </v-card>
      </template>
    </v-stepper>

    <template v-slot:configuration>
      <v-text-field v-model="prev" label="Previous text"></v-text-field>

      <v-text-field v-model="next" label="Next text"></v-text-field>

      <v-checkbox v-model="hideActions" label="Hide actions"></v-checkbox>

      <v-checkbox v-model="editable" label="Editable"></v-checkbox>

      <v-checkbox v-model="altLabels" label="Alt labels"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-stepper'
  const model = ref('default')
  const options = []
  const step = ref(1)
  const altLabels = ref(false)
  const editable = ref(false)
  const hideActions = ref(false)
  const prev = ref('$vuetify.stepper.prev')
  const next = ref('$vuetify.stepper.next')

  function onDblClick (e) {
    e.target.contentEditable = true
  }

  function onBlur (e) {
    e.target.contentEditable = false
  }

  const props = computed(() => {
    return {
      'alt-labels': altLabels.value || undefined,
      editable: editable.value || undefined,
      'hide-actions': hideActions.value || undefined,
      'prev-text': prev.value.startsWith('$vuetify') ? undefined : prev.value,
      'next-text': next.value.startsWith('$vuetify') ? undefined : next.value,
      items: [
        'Step 1',
        'Step 2',
        'Step 3',
      ],
    }
  })

  const slots = computed(() => {
    return `
  <template v-slot:item.1>
    <v-card title="Step One" flat>...</v-card>
  </template>

  <template v-slot:item.2>
    <v-card title="Step Two" flat>...</v-card>
  </template>

  <template v-slot:item.3>
    <v-card title="Step Three" flat>...</v-card>
  </template>
`
  })

  const code = computed(() => {
    return `<v-stepper${propsToString(props.value)}>${slots.value}</v-stepper>`
  })
</script>

```

# Vuetify component v-stepper - misc linear

Example code

```vue
<template>
  <v-stepper>
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad group"
        value="2"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>

  <br>

  <v-stepper model-value="2">
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad group"
        value="2"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>

  <br>

  <v-stepper model-value="3">
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad group"
        value="2"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - misc dynamic

Example code

```vue
<template>
  <div>
    <v-card class="mb-4">
      <v-card-text>
        <v-select
          v-model="steps"
          :items="[2, 3, 4, 5, 6]"
          label="# of steps"
        ></v-select>
      </v-card-text>
    </v-card>

    <v-stepper v-model="e1">
      <template v-slot:default="{ prev, next }">
        <v-stepper-header>
          <template v-for="n in steps" :key="`${n}-step`">
            <v-stepper-item
              :complete="e1 > n"
              :step="`Step {{ n }}`"
              :value="n"
              editable
            ></v-stepper-item>

            <v-divider
              v-if="n !== steps"
              :key="n"
            ></v-divider>
          </template>
        </v-stepper-header>

        <v-stepper-window>
          <v-stepper-window-item
            v-for="n in steps"
            :key="`${n}-content`"
            :value="n"
          >
            <v-card
              color="grey-lighten-1"
              height="200"
            ></v-card>
          </v-stepper-window-item>
        </v-stepper-window>

        <v-stepper-actions
          :disabled="disabled"
          @click:next="next"
          @click:prev="prev"
        ></v-stepper-actions>
      </template>
    </v-stepper>
  </div>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const e1 = ref(1)
  const steps = ref(2)

  const disabled = computed(() => {
    return e1.value === 1 ? 'prev' : e1.value === steps.value ? 'next' : undefined
  })
</script>

<script>
  export default {
    data () {
      return {
        e1: 1,
        steps: 2,
      }
    },

    computed: {
      disabled () {
        return this.e1 === 1 ? 'prev' : this.e1 === this.steps ? 'next' : undefined
      },
    },
  }
</script>

```

# Vuetify component v-stepper - prop mobile

Example code

```vue
<template>
  <v-stepper mobile>
    <v-stepper-header>
      <template v-for="(item, i) in items" :key="i">
        <v-divider v-if="i"></v-divider>

        <v-stepper-item v-bind="item"></v-stepper-item>
      </template>
    </v-stepper-header>
  </v-stepper>
</template>

<script setup>
  const items = Array.from({ length: 10 }).map((_, i) => ({
    title: `Step ${i + 1}`,
    subtitle: `Step ${i + 1} subtitle`,
    value: i + 1,
  }))
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 10 }).map((_, i) => ({
        title: `Step ${i + 1}`,
        subtitle: `Step ${i + 1} subtitle`,
        value: i + 1,
      })),
    }),
  }
</script>

```

# Vuetify component v-stepper - misc alternate error

Example code

```vue
<template>
  <v-stepper alt-labels>
    <v-stepper-header>
      <v-stepper-item
        value="1"
        complete
      >
        <template v-slot:title>
          Ad type
        </template>
      </v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        value="2"
        complete
      >
        <template v-slot:title>
          Ad style
        </template>
      </v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        :rules="[() => false]"
        value="3"
      >
        <template v-slot:title>
          Custom channels
        </template>

        <template v-slot:subtitle>
          Alert message
        </template>
      </v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item value="46">
        <template v-slot:title>
          Get code
        </template>
      </v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - misc non editable

Example code

```vue
<template>
  <v-stepper model-value="2">
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad group"
        value="2"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - prop alternate label

Example code

```vue
<template>
  <v-stepper alt-labels>
    <v-stepper-header>
      <v-stepper-item title="Ad unit details" value="1"></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item title="Ad sizes" value="2"></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item title="Ad templates" value="3"></v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - misc optional

Example code

```vue
<template>
  <v-stepper model-value="1">
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        subtitle="Optional"
        title="Create an ad group"
        value="2"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>

  <br>

  <v-stepper model-value="2">
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        subtitle="Optional"
        title="Create an ad group"
        value="2"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - misc vertical error

Example code

```vue
<template>
  <v-stepper
    v-model="e13"
    vertical
  >
    <v-stepper-step
      step="1"
      complete
    >
      Name of step 1
    </v-stepper-step>

    <v-stepper-content step="1">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e13 = 2"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step
      step="2"
      complete
    >
      Name of step 2
    </v-stepper-step>

    <v-stepper-content step="2">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e13 = 3"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step
      :rules="[() => false]"
      step="3"
    >
      Ad templates
      <small>Alert message</small>
    </v-stepper-step>

    <v-stepper-content step="3">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e13 = 4"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step step="4">
      View setup instructions
    </v-stepper-step>

    <v-stepper-content step="4">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e13 = 1"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script setup>
  import { ref } from 'vue'

  const e13 = ref(2)
</script>

<script>
  export default {
    data () {
      return {
        e13: 2,
      }
    },
  }
</script>

```

# Vuetify component v-stepper - misc error

Example code

```vue
<template>
  <v-stepper model-value="3">
    <v-stepper-header>
      <v-stepper-item
        title="Job Search"
        value="1"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        :rules="[() => false]"
        subtitle="Missing Details"
        title="Submit Application"
        value="2"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Interview Process"
        value="3"
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Hiring Decision"
        value="4"
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - misc horizontal

Example code

```vue
<template>
  <v-stepper
    v-model="step"
    :items="items"
    show-actions
  >
    <template v-slot:item.1>
      <h3 class="text-h6">Order</h3>

      <br>

      <v-sheet border>
        <v-table>
          <thead>
            <tr>
              <th>Description</th>
              <th class="text-end">Quantity</th>
              <th class="text-end">Price</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(product, index) in products" :key="index">
              <td v-text="product.name"></td>
              <td class="text-end" v-text="product.quantity"></td>
              <td class="text-end" v-text="product.quantity * product.price"></td>
            </tr>

            <tr>
              <th>Total</th>
              <th></th>
              <th class="text-end">
                ${{ subtotal }}
              </th>
            </tr>
          </tbody>
        </v-table>
      </v-sheet>
    </template>

    <template v-slot:item.2>
      <h3 class="text-h6">Shipping</h3>

      <br>

      <v-radio-group v-model="shipping" label="Delivery Method">
        <v-radio label="Standard Shipping" value="5"></v-radio>
        <v-radio label="Priority Shipping" value="10"></v-radio>
        <v-radio label="Express Shipping" value="15"></v-radio>
      </v-radio-group>
    </template>

    <template v-slot:item.3>
      <h3 class="text-h6">Confirm</h3>

      <br>

      <v-sheet border>
        <v-table>
          <thead>
            <tr>
              <th>Description</th>
              <th class="text-end">Quantity</th>
              <th class="text-end">Price</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(product, index) in products" :key="index">
              <td v-text="product.name"></td>
              <td class="text-end" v-text="product.quantity"></td>
              <td class="text-end" v-text="product.quantity * product.price"></td>
            </tr>

            <tr>
              <td>Shipping</td>
              <td></td>
              <td class="text-end" v-text="shipping"></td>
            </tr>

            <tr>
              <th>Total</th>
              <th></th>
              <th class="text-end">
                ${{ total }}
              </th>
            </tr>
          </tbody>
        </v-table>
      </v-sheet>
    </template>
  </v-stepper>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const shipping = ref(0)
  const step = ref(1)
  const subtotal = computed(() => products.reduce((acc, product) => acc + product.quantity * product.price, 0))
  const total = computed(() => subtotal.value + Number(shipping.value ?? 0))

  const items = [
    'Review Order',
    'Select Shipping',
    'Submit',
  ]
  const products = [
    {
      name: 'Product 1',
      price: 10,
      quantity: 2,
    },
    {
      name: 'Product 2',
      price: 15,
      quantity: 10,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      shipping: 0,
      step: 1,
      items: [
        'Review Order',
        'Select Shipping',
        'Submit',
      ],
      products: [
        {
          name: 'Product 1',
          price: 10,
          quantity: 2,
        },
        {
          name: 'Product 2',
          price: 15,
          quantity: 10,
        },
      ],
    }),

    computed: {
      subtotal () {
        return this.products.reduce((acc, product) => acc + product.quantity * product.price, 0)
      },
      total () {
        return this.subtotal + Number(this.shipping ?? 0)
      },
    },
  }
</script>

```

# Vuetify component v-stepper - misc editable

Example code

```vue
<template>
  <v-stepper>
    <v-stepper-header>
      <v-stepper-item
        title="Select campaign settings"
        value="1"
        complete
        editable
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad group"
        value="2"
        complete
      ></v-stepper-item>

      <v-divider></v-divider>

      <v-stepper-item
        title="Create an ad"
        value="3"
        editable
      ></v-stepper-item>
    </v-stepper-header>
  </v-stepper>
</template>

```

# Vuetify component v-stepper - prop vertical

Example code

```vue
<template>
  <v-stepper
    v-model="e6"
    vertical
  >
    <v-stepper-step
      :complete="e6 > 1"
      step="1"
    >
      Select an app
      <small>Summarize if needed</small>
    </v-stepper-step>

    <v-stepper-content step="1">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e6 = 2"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step
      :complete="e6 > 2"
      step="2"
    >
      Configure analytics for this app
    </v-stepper-step>

    <v-stepper-content step="2">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e6 = 3"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step
      :complete="e6 > 3"
      step="3"
    >
      Select an ad format and name ad unit
    </v-stepper-step>

    <v-stepper-content step="3">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e6 = 4"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>

    <v-stepper-step step="4">
      View setup instructions
    </v-stepper-step>
    <v-stepper-content step="4">
      <v-card
        class="mb-12"
        color="grey-lighten-1"
        height="200px"
      ></v-card>
      <v-btn
        color="primary"
        @click="e6 = 1"
      >
        Continue
      </v-btn>
      <v-btn variant="text">
        Cancel
      </v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script setup>
  import { ref } from 'vue'

  const e6 = ref(1)
</script>

<script>
  export default {
    data () {
      return {
        e6: 1,
      }
    },
  }
</script>

```

# Vuetify component v-stepper - prop non linear

Example code

```vue
<template>
  <div>
    <v-stepper non-linear>
      <v-stepper-header>
        <v-stepper-item
          value="1"
          editable
        >
          Select campaign settings
        </v-stepper-item>

        <v-divider></v-divider>

        <v-stepper-item
          value="2"
          editable
        >
          Create an ad group
        </v-stepper-item>

        <v-divider></v-divider>

        <v-stepper-item
          value="3"
          editable
        >
          Create an ad
        </v-stepper-item>
      </v-stepper-header>
    </v-stepper>

    <v-stepper
      class="mt-12"
      non-linear
    >
      <v-stepper-header>
        <v-stepper-item
          value="1"
          complete
          editable
        >
          Select campaign settings
        </v-stepper-item>

        <v-divider></v-divider>

        <v-stepper-item
          value="2"
          editable
        >
          Create an ad group
        </v-stepper-item>

        <v-divider></v-divider>

        <v-stepper-item
          value="3"
          complete
          editable
        >
          Create an ad
        </v-stepper-item>
      </v-stepper-header>
    </v-stepper>

    <v-stepper
      class="mt-12"
      value="3"
      non-linear
    >
      <v-stepper-header>
        <v-stepper-item
          value="1"
          complete
          editable
        >
          Select campaign settings
        </v-stepper-item>

        <v-divider></v-divider>

        <v-stepper-item
          value="2"
          complete
          editable
        >
          Create an ad group
        </v-stepper-item>

        <v-divider></v-divider>

        <v-stepper-item
          value="3"
          complete
          editable
        >
          Create an ad
        </v-stepper-item>
      </v-stepper-header>
    </v-stepper>
  </div>
</template>

```
