# Vuetify component v-date-picker - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-date-picker
      v-bind="props"
      v-model="date"
      class="mx-auto"
    ></v-date-picker>

    <template v-slot:configuration>
      <!-- <v-checkbox v-model="hideActions" label="Hide actions"></v-checkbox> -->
      <v-checkbox v-model="adjacent" label="Show adjacent months"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-date-picker'
  const model = ref('default')
  const date = ref()
  const options = []
  // const hideActions = ref(false)
  const adjacent = ref(false)

  const props = computed(() => {
    return {
      // 'hide-actions': hideActions.value || undefined,
      'show-adjacent-months': adjacent.value || undefined,
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<v-date-picker${propsToString(props.value)}>${slots.value}</v-date-picker>`
  })
</script>

```

# Vuetify component v-date-picker - misc formatting

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        lg="6"
      >
        <v-menu
          ref="menu1"
          v-model="menu1Active"
          :close-on-content-click="false"
          max-width="290px"
          min-width="auto"
          transition="scale-transition"
        >
          <template v-slot:activator="{ props }">
            <v-text-field
              v-model="dateFormatted"
              hint="MM/DD/YYYY format"
              label="Date"
              prepend-icon="mdi-calendar"
              persistent-hint
              v-bind="props"
              @blur="date = parseDate(dateFormatted)"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            no-title
            @input="menu1 = false"
          ></v-date-picker>
        </v-menu>
        <p>Date in ISO format: <strong>{{ date }}</strong></p>
      </v-col>

      <v-col
        cols="12"
        lg="6"
      >
        <v-menu
          v-model="menu2"
          :close-on-content-click="false"
          max-width="290px"
          min-width="auto"
          transition="scale-transition"
        >
          <template v-slot:activator="{ props }">
            <v-text-field
              v-model="computedDateFormatted"
              hint="MM/DD/YYYY format"
              label="Date (read only text field)"
              prepend-icon="mdi-calendar"
              persistent-hint
              readonly
              v-bind="props"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            no-title
            @input="menu2 = false"
          ></v-date-picker>
        </v-menu>
        <p>Date in ISO format: <strong>{{ date }}</strong></p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { computed, ref, watch } from 'vue'

  const menu1 = ref()

  const date = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  const dateFormatted = ref(formatDate((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)))
  const menu1Active = ref(false)
  const menu2 = ref(false)

  const computedDateFormatted = computed(() => {
    return formatDate(date.value)
  })

  watch(date, val => {
    dateFormatted.value = formatDate(val)
  })

  function formatDate (date) {
    if (!date) return null
    const [year, month, day] = date.split('-')
    return `${month}/${day}/${year}`
  }
  function parseDate (date) {
    if (!date) return null
    const [month, day, year] = date.split('/')
    return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
  }
</script>

<script>
  export default {
    data: vm => ({
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      dateFormatted: vm.formatDate((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)),
      menu1: false,
      menu2: false,
    }),

    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },

    watch: {
      date (val) {
        this.dateFormatted = this.formatDate(this.date)
      },
    },

    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${month}/${day}/${year}`
      },
      parseDate (date) {
        if (!date) return null

        const [month, day, year] = date.split('/')
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
      },
    },
  }
</script>

```

# Vuetify component v-date-picker - prop show adjacent months

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-date-picker show-adjacent-months></v-date-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-date-picker - misc dialog and menu

Example code

```vue
<template>
  <v-row>
    <v-col
      cols="12"
      md="4"
      sm="6"
    >
      <v-menu
        ref="menu"
        v-model="menuActive"
        v-model:return-value="date"
        :close-on-content-click="false"
        min-width="auto"
        transition="scale-transition"
      >
        <template v-slot:activator="{ props }">
          <v-text-field
            v-model="date"
            label="Picker in menu"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="props"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="date"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            variant="text"
            @click="menu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            variant="text"
            @click="menu.save(date)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
    <v-spacer></v-spacer>
    <v-col
      cols="12"
      md="4"
      sm="6"
    >
      <v-dialog
        ref="dialog"
        v-model="modal"
        width="290px"
        persistent
      >
        <template v-slot:activator="{ props }">
          <v-text-field
            v-model="date"
            label="Picker in dialog"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="props"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="date"
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            variant="text"
            @click="modal = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            variant="text"
            @click="dialog.save(date)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-dialog>
    </v-col>
    <v-col
      cols="12"
      md="4"
      sm="6"
    >
      <v-menu
        v-model="menu2"
        :close-on-content-click="false"
        min-width="auto"
        transition="scale-transition"
      >
        <template v-slot:activator="{ props }">
          <v-text-field
            v-model="date"
            label="Picker without buttons"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="props"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="date"
          @change="menu2 = false"
        ></v-date-picker>
      </v-menu>
    </v-col>
    <v-spacer></v-spacer>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const menu = ref()

  const date = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  const menuActive = ref(false)
  const modal = ref(false)
  const menu2 = ref(false)
</script>

<script>
  export default {
    data: () => ({
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      menuActive: false,
      modal: false,
      menu2: false,
    }),
  }
</script>

```

# Vuetify component v-date-picker - prop width

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-date-picker width="400"></v-date-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-date-picker - guide locale

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-locale-provider locale="sv">
      <v-date-picker></v-date-picker>
    </v-locale-provider>
  </div>
</template>

<playground-resources lang="json">
{
  "imports": {
    "vuetify/locale": "https://cdn.jsdelivr.net/npm/vuetify/lib/locale/index.js/+esm",
    "@date-io/date-fns": "https://cdn.jsdelivr.net/npm/@date-io/date-fns@2.17.0/build/index.esm.js/+esm",
    "date-fns/locale/en-US": "https://cdn.jsdelivr.net/npm/date-fns@2.30.0/esm/locale/en-US/index.js/+esm",
    "date-fns/locale/sv": "https://cdn.jsdelivr.net/npm/date-fns@2.30.0/esm/locale/sv/index.js/+esm"
  }
}
</playground-resources>

<playground-setup>
import { createVuetify } from 'vuetify'
import { sv } from 'vuetify/locale'
import DateFnsAdapter from '@date-io/date-fns'
import enUS from 'date-fns/locale/en-US'
import svSE from 'date-fns/locale/sv'

export const vuetify = createVuetify({
  locale: {
    messages: { sv },
  },
  date: {
    adapter: DateFnsAdapter,
    locale: {
      en: enUS,
      sv: svSE,
    },
  },
})
</playground-setup>

```

# Vuetify component v-date-picker - prop multiple

Example code

```vue
<template>
  <v-row>
    <v-col
      cols="12"
      sm="6"
    >
      <v-date-picker
        v-model="dates"
        multiple
      ></v-date-picker>
    </v-col>
    <v-col
      cols="12"
      sm="6"
    >
      <v-menu
        ref="menu"
        v-model="menuActive"
        v-model:return-value="dates"
        :close-on-content-click="false"
        min-width="auto"
        transition="scale-transition"
      >
        <template v-slot:activator="{ props }">
          <v-combobox
            v-model="dates"
            label="Multiple picker in menu"
            prepend-icon="mdi-calendar"
            chips
            multiple
            readonly
            v-bind="props"
          ></v-combobox>
        </template>
        <v-date-picker
          v-model="dates"
          multiple
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            variant="text"
            @click="menu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            variant="text"
            @click="menu.save(dates)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const menu = ref()

  const dates = ref(['2018-09-15', '2018-09-20'])
  const menuActive = ref(false)
</script>

<script>
  export default {
    data: () => ({
      dates: ['2018-09-15', '2018-09-20'],
      menuActive: false,
    }),
  }
</script>

```

# Vuetify component v-date-picker - prop elevation

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-date-picker elevation="24"></v-date-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-date-picker - misc formatting external libraries

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        lg="6"
      >
        <v-menu
          v-model="menu1"
          :close-on-content-click="false"
          max-width="290"
        >
          <template v-slot:activator="{ props }">
            <v-text-field
              :model-value="computedDateFormattedMomentjs"
              label="Formatted with Moment.js"
              clearable
              readonly
              v-bind="props"
              @click:clear="date = null"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            @change="menu1 = false"
          ></v-date-picker>
        </v-menu>
      </v-col>

      <v-col
        cols="12"
        lg="6"
      >
        <v-menu
          v-model="menu2"
          :close-on-content-click="false"
          max-width="290"
        >
          <template v-slot:activator="{ props }">
            <v-text-field
              :model-value="computedDateFormattedDatefns"
              label="Formatted with datefns"
              clearable
              readonly
              v-bind="props"
              @click:clear="date = null"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            @change="menu2 = false"
          ></v-date-picker>
        </v-menu>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { computed, ref } from 'vue'
  import moment from 'moment'
  import { format, parseISO } from 'date-fns'

  const date = ref(format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'))
  const menu1 = ref(false)
  const menu2 = ref(false)

  const computedDateFormattedMomentjs = computed(() => {
    return date.value ? moment(date.value).format('dddd, MMMM Do YYYY') : ''
  })
  const computedDateFormattedDatefns = computed(() => {
    return date.value ? format(parseISO(date.value), 'EEEE, MMMM do yyyy') : ''
  })
</script>

<script>
  import moment from 'moment'
  import { format, parseISO } from 'date-fns'

  export default {
    data: () => ({
      // https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments
      date: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
      menu1: false,
      menu2: false,
    }),

    computed: {
      computedDateFormattedMomentjs () {
        return this.date ? moment(this.date).format('dddd, MMMM Do YYYY') : ''
      },
      computedDateFormattedDatefns () {
        return this.date ? format(parseISO(this.date), 'EEEE, MMMM do yyyy') : ''
      },
    },
  }
</script>

<playground-resources lang="json">
  {
    "imports": {
      "moment": "https://cdn.jsdelivr.net/npm/moment@2.29.4/moment.min.js",
      "date-fns": "https://cdn.jsdelivr.net/npm/date-fns@2.30.0/esm/index.js/+esm"
    }
  }
</playground-resources>

```

# Vuetify component v-date-picker - misc birthday

Example code

```vue
<template>
  <div>
    <div class="mb-6">Active picker: <code>{{ activePicker || 'null' }}</code></div>
    <v-menu
      ref="menu"
      v-model="menuActive"
      :close-on-content-click="false"
      min-width="auto"
      transition="scale-transition"
    >
      <template v-slot:activator="{ props }">
        <v-text-field
          v-model="date"
          label="Birthday date"
          prepend-icon="mdi-calendar"
          readonly
          v-bind="props"
        ></v-text-field>
      </template>
      <v-date-picker
        v-model="date"
        v-model:active-picker="activePicker"
        :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
        min="1950-01-01"
        @change="save"
      ></v-date-picker>
    </v-menu>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const menu = ref()

  const activePicker = ref(null)
  const date = ref(null)
  const menuActive = ref(false)

  watch(menuActive, val => {
    val && setTimeout(() => (activePicker.value = 'YEAR'))
  })

  function save (date) {
    menu.value.save(date)
  }
</script>

<script>
  export default {
    data: () => ({
      activePicker: null,
      date: null,
      menuActive: false,
    }),
    watch: {
      menuActive (val) {
        val && setTimeout(() => (this.activePicker = 'YEAR'))
      },
    },
    methods: {
      save (date) {
        this.$refs.menu.save(date)
      },
    },
  }
</script>

```

# Vuetify component v-date-picker - prop icons

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="picker"
      next-icon="mdi-skip-next"
      prev-icon="mdi-skip-previous"
      year-icon="mdi-calendar-blank"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
</script>

<script>
  export default {
    data () {
      return {
        picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker - prop readonly

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="date"
      readonly
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const date = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
</script>

<script>
  export default {
    data () {
      return {
        date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker - prop range

Example code

```vue
<template>
  <v-row>
    <v-col
      cols="12"
      sm="6"
    >
      <v-date-picker
        v-model="dates"
        range
      ></v-date-picker>
    </v-col>
    <v-col
      cols="12"
      sm="6"
    >
      <v-text-field
        v-model="dateRangeText"
        label="Date range"
        prepend-icon="mdi-calendar"
        readonly
      ></v-text-field>
      model: {{ dates }}
    </v-col>
  </v-row>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const dates = ref(['2019-09-10', '2019-09-20'])
  const dateRangeText = computed(() => {
    return dates.value.join(' ~ ')
  })
</script>

<script>
  export default {
    data: () => ({
      dates: ['2019-09-10', '2019-09-20'],
    }),
    computed: {
      dateRangeText () {
        return this.dates.join(' ~ ')
      },
    },
  }
</script>

```

# Vuetify component v-date-picker - event button events

Example code

```vue
<template>
  <v-row>
    <v-col
      class="my-2 px-1"
      cols="12"
      sm="6"
    >
      <v-date-picker
        v-model="date"
        @contextmenu:year="contextMenu"
        @dblclick:date="dblClick"
        @mouseenter:month="mouseEnter"
        @mouseleave:month="mouseLeave"
      ></v-date-picker>
    </v-col>

    <v-col
      class="my-2 px-1"
      cols="12"
      sm="6"
    >
      <div class="text-body-1 mb-2">
        <v-icon size="small">
          {{ done[0] ? '$checkboxOn' : '$checkboxOff' }}
        </v-icon>
        Double click on any date
      </div>

      <div class="text-body-1">
        <v-icon size="small">
          {{ done[1] ? '$checkboxOn' : '$checkboxOff' }}
        </v-icon>
        Move mouse cursor over any month button
      </div>

      <div class="text-h6 mb-2">
        Mouse pointer is located on: {{ mouseMonth || '-' }}
      </div>

      <div class="text-body-1">
        <v-icon size="small">
          {{ done[2] ? '$checkboxOn' : '$checkboxOff' }}
        </v-icon>
        Right click on any year
      </div>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const date = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  const done = ref([false, false, false])
  const mouseMonth = ref(null)

  function contextMenu (year, event) {
    done.value[2] = true
    event.preventDefault()
    alert(`You have activated context menu for year ${year}`)
  }
  function dblClick (date) {
    done.value[0] = true
    alert(`You have just double clicked the following date: ${date}`)
  }
  function mouseEnter (month) {
    done.value[1] = true
    mouseMonth.value = month
  }
  function mouseLeave () {
    mouseMonth.value = null
  }
</script>

<script>
  export default {
    data: () => ({
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      done: [false, false, false],
      mouseMonth: null,
    }),

    methods: {
      contextMenu (year, event) {
        this.done[2] = true

        event.preventDefault()

        alert(`You have activated context menu for year ${year}`)
      },
      dblClick (date) {
        this.done[0] = true

        alert(`You have just double clicked the following date: ${date}`)
      },
      mouseEnter (month) {
        this.done[1] = true
        this.mouseMonth = month
      },
      mouseLeave () {
        this.mouseMonth = null
      },
    },
  }
</script>

```

# Vuetify component v-date-picker - misc orientation

Example code

```vue
<template>
  <v-row align="center">
    <v-checkbox
      v-model="landscape"
      label="Landscape"
    ></v-checkbox>
    <v-date-picker
      v-model="picker"
      :landscape="landscape"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(new Date().toISOString().substr(0, 7))
  const landscape = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        picker: new Date().toISOString().substr(0, 7),
        landscape: false,
      }
    },
  }
</script>

```

# Vuetify component v-date-picker - prop show current

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-date-picker
      v-model="date1"
      :show-current="false"
    ></v-date-picker>
    <v-date-picker
      v-model="date2"
      show-current="2013-07-13"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const date1 = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  const date2 = ref('2013-07-29')
</script>

<script>
  export default {
    data () {
      return {
        date1: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        date2: '2013-07-29',
      }
    },
  }
</script>

```

# Vuetify component v-date-picker - misc internationalization

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-date-picker
      v-model="picker"
      :first-day-of-week="0"
      locale="zh-cn"
    ></v-date-picker>
    <v-date-picker
      v-model="picker"
      :first-day-of-week="1"
      locale="sv-se"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
</script>

<script>
  export default {
    data () {
      return {
        picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker - prop picker date

Example code

```vue
<template>
  <v-row>
    <v-col
      class="my-2 px-1"
      cols="12"
      sm="6"
    >
      <v-date-picker
        ref="picker"
        v-model="date"
        v-model:picker-date="pickerDate"
        full-width
      ></v-date-picker>
    </v-col>
    <v-col
      class="my-2 px-1"
      cols="12"
      sm="6"
    >
      <div class="text-h6">
        Month news ({{ pickerDate || 'change month...' }})
      </div>
      <div class="subheading">
        Change month to see other news
      </div>
      <ul class="ma-4">
        <li
          v-for="note in notes"
          :key="note"
        >
          {{ note }}
        </li>
      </ul>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const allNotes = [
    'President met with prime minister',
    'New power plant opened',
    'Rocket launch announced',
    'Global warming discussion cancelled',
    'Company changed its location',
  ]

  const date = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  const pickerDate = ref(null)
  const notes = ref([])

  watch(pickerDate, val => {
    notes.value = [
      allNotes[Math.floor(Math.random() * 5)],
      allNotes[Math.floor(Math.random() * 5)],
      allNotes[Math.floor(Math.random() * 5)],
    ].filter((value, index, self) => self.indexOf(value) === index)
  })
</script>

<script>
  export default {
    data: () => ({
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      pickerDate: null,
      notes: [],
      allNotes: [
        'President met with prime minister',
        'New power plant opened',
        'Rocket launch announced',
        'Global warming discussion cancelled',
        'Company changed its location',
      ],
    }),
    watch: {
      pickerDate (val) {
        this.notes = [
          this.allNotes[Math.floor(Math.random() * 5)],
          this.allNotes[Math.floor(Math.random() * 5)],
          this.allNotes[Math.floor(Math.random() * 5)],
        ].filter((value, index, self) => self.indexOf(value) === index)
      },
    },
  }
</script>

```

# Vuetify component v-date-picker - prop colors

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-date-picker
        color="primary"
      ></v-date-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-date-picker - event events

Example code

```vue
<template>
  <v-row justify="space-between">
    <div>
      <div class="subheading">
        Defined by array
      </div>
      <v-date-picker
        v-model="date1"
        :events="arrayEvents"
        event-color="green lighten-1"
      ></v-date-picker>
    </div>
    <div>
      <div class="subheading">
        Defined by function
      </div>
      <v-date-picker
        v-model="date2"
        :event-color="date => date[9] % 2 ? 'red' : 'yellow'"
        :events="functionEvents"
      ></v-date-picker>
    </div>
  </v-row>
</template>

<script setup>
  import { onMounted, ref } from 'vue'

  const arrayEvents = ref(null)
  const date1 = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  const date2 = ref((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
  function functionEvents (date) {
    const [, , day] = date.split('-')
    if ([12, 17, 28].includes(parseInt(day, 10))) return true
    if ([1, 19, 22].includes(parseInt(day, 10))) return ['red', '#00f']
    return false
  }
  onMounted(() => {
    arrayEvents.value = [...Array(6)].map(() => {
      const day = Math.floor(Math.random() * 30)
      const d = new Date()
      d.setDate(day)
      return d.toISOString().substr(0, 10)
    })
  })
</script>

<script>
  export default {
    data: () => ({
      arrayEvents: null,
      date1: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      date2: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    }),

    mounted () {
      this.arrayEvents = [...Array(6)].map(() => {
        const day = Math.floor(Math.random() * 30)
        const d = new Date()
        d.setDate(day)
        return d.toISOString().substr(0, 10)
      })
    },

    methods: {
      functionEvents (date) {
        const [,, day] = date.split('-')
        if ([12, 17, 28].includes(parseInt(day, 10))) return true
        if ([1, 19, 22].includes(parseInt(day, 10))) return ['red', '#00f']
        return false
      },
    },
  }
</script>

```

# Vuetify component v-date-picker - prop allowed dates

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-date-picker
        v-model="date"
        :allowed-dates="allowedDates"
        max="2018-03-20"
        min="2016-06-15"
      ></v-date-picker>
    </v-row>
  </v-container>
</template>

<script setup>
  import { useDate } from 'vuetify'
  import { ref } from 'vue'

  const date = ref(new Date('2018-03-02'))
  const adapter = useDate()

  function allowedDates (val) {
    return parseInt(adapter.toISO(val).split('-')[2], 10) % 2 === 0
  }
</script>

<script>
  export default {
    data: () => ({
      date: new Date('2018-03-02'),
    }),

    methods: {
      allowedDates: val => {
        return parseInt(this.$vuetify.date.toISO(val).split('-')[2], 10) % 2 === 0
      },
    },
  }
</script>

```
