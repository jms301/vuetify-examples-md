# Vuetify concept application-layout - nav drawer first

Example code

```vue
<template>
  <v-layout class="rounded rounded-md border">
    <v-navigation-drawer>
      <v-list nav>
        <v-list-item title="Navigation drawer" link></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar title="Application bar"></v-app-bar>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="200"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>
  </v-layout>
</template>

```

# Vuetify concept application-layout - layout information ref

Example code

```vue
<template>
  <v-layout ref="app" class="rounded rounded-md border">
    <v-app-bar color="surface-light" name="app-bar">
      <v-btn class="mx-auto" @click="print('app-bar')">Get data</v-btn>
    </v-app-bar>

    <v-navigation-drawer
      color="surface-variant"
      location="end"
      name="drawer"
      permanent
    >
      <div class="d-flex justify-center align-center h-100">
        <v-btn variant="text" @click="print('drawer')">Get data</v-btn>
      </div>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="150"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>

    <v-footer color="surface-light" name="footer" app>
      <v-btn
        class="mx-auto"
        text="Get data"
        variant="text"
        @click="print('footer')"
      ></v-btn>
    </v-footer>
  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const app = ref()

  function print (key) {
    alert(JSON.stringify(app.value.getLayoutItem(key), null, 2))
  }
</script>

<script>
  export default {
    methods: {
      print (key) {
        alert(JSON.stringify(this.$refs.app.getLayoutItem(key), null, 2))
      },
    },
  }
</script>

```

# Vuetify concept application-layout - layout information composable

Example code

```vue
<template>
  <v-layout ref="app" class="rounded rounded-md border">
    <v-app-bar color="surface-variant" name="app-bar">
      <child v-slot="{ print }">
        <v-btn class="mx-auto" @click="print('app-bar')">Get data</v-btn>
      </child>
    </v-app-bar>

    <v-navigation-drawer
      color="surface-light"
      name="drawer"
      permanent
    >
      <div class="d-flex justify-center align-center h-100">
        <child v-slot="{ print }">
          <v-btn variant="text" @click="print('drawer')">Get data</v-btn>
        </child>
      </div>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="150"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>

    <v-footer color="surface-light" name="footer" app>
      <v-btn
        class="mx-auto"
        text="Get data"
        variant="text"
        @click="print('footer')"
      ></v-btn>
    </v-footer>
  </v-layout>
</template>

<script setup>
  import { useLayout } from 'vuetify'

  const Child = {
    setup (props, ctx) {
      const { getLayoutItem } = useLayout()

      function print (key) {
        alert(JSON.stringify(getLayoutItem(key), null, 2))
      }

      return () => ctx.slots.default({ print })
    },
  }
</script>

<script>
  import { useLayout } from 'vuetify'

  const Child = {
    setup (props, ctx) {
      const { getLayoutItem } = useLayout()

      function print (key) {
        alert(JSON.stringify(getLayoutItem(key), null, 2))
      }

      return () => ctx.slots.default({ print })
    },
  }

  export default {
    components: { Child },
  }
</script>

```

# Vuetify concept application-layout - dynamic

Example code

```vue
<template>
  <v-layout class="rounded rounded-md border">
    <v-navigation-drawer color="surface-variant" permanent></v-navigation-drawer>

    <v-app-bar
      :order="order"
      color="grey-lighten-2"
      title="Application bar"
      flat
    >
      <template v-slot:append>
        <v-switch
          v-model="order"
          class="me-2"
          false-value="0"
          label="Toggle order"
          true-value="-1"
          hide-details
          inset
        ></v-switch>
      </template>
    </v-app-bar>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="200"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>
  </v-layout>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const order = shallowRef(0)
</script>

<script>
  export default {
    data: () => ({
      order: 0,
    }),
  }
</script>

```

# Vuetify concept application-layout - location

Example code

```vue
<template>
  <v-layout class="rounded rounded-md border">
    <v-app-bar color="surface-variant" title="Application bar"></v-app-bar>

    <v-navigation-drawer>
      <v-list nav>
        <v-list-item title="Drawer left" link></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer location="right">
      <v-list nav>
        <v-list-item title="Drawer right" link></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="200"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>
  </v-layout>
</template>

```

# Vuetify concept application-layout - discord

Example code

```vue
<template>
  <v-layout class="rounded rounded-md">
    <v-system-bar color="grey-darken-3"></v-system-bar>

    <v-navigation-drawer
      color="grey-darken-2"
      width="72"
      permanent
    ></v-navigation-drawer>

    <v-navigation-drawer
      color="grey-darken-1"
      width="150"
      permanent
    ></v-navigation-drawer>

    <v-app-bar
      color="grey"
      height="48"
      flat
    ></v-app-bar>

    <v-navigation-drawer
      color="grey-lighten-1"
      location="right"
      width="150"
      permanent
    ></v-navigation-drawer>

    <v-app-bar
      color="grey-lighten-2"
      height="48"
      location="bottom"
      flat
    ></v-app-bar>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="150"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>
  </v-layout>
</template>

```

# Vuetify concept application-layout - app bar first

Example code

```vue
<template>
  <v-layout class="rounded rounded-md border">
    <v-app-bar title="Application bar"></v-app-bar>

    <v-navigation-drawer>
      <v-list nav>
        <v-list-item title="Navigation drawer" link></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" height="300">
      <v-container>
        <v-sheet
          border="dashed md"
          color="surface-light"
          height="200"
          rounded="lg"
          width="100%"
        ></v-sheet>
      </v-container>
    </v-main>
  </v-layout>
</template>

```
