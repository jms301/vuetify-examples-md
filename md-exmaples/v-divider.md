# Vuetify component v-divider - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="d-flex align-center justify-center" style="height: 200px;">
      <v-divider v-bind="props"></v-divider>
    </div>

    <template v-slot:configuration>
      <v-slider v-model="thickness" label="Thickness" max="20" min="1"></v-slider>

      <v-select v-model="opacity" :items="opacities" label="Opacity"></v-select>

      <v-select v-model="color" :items="colors" label="Color"></v-select>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-divider'
  const model = ref('default')
  const color = ref()
  const opacity = ref('default')
  const thickness = ref(1)
  const colors = [
    'success',
    'info',
    'warning',
    'error',
  ]
  const opacities = [100, 75, 50, 25, 'default', 0]
  const options = ['inset', 'vertical']
  const props = computed(() => {
    let classes

    if (opacity.value != null && opacity.value !== 'default') {
      classes = `border-opacity-${opacity.value}`
    }
    return {
      thickness: thickness.value !== 1 ? thickness.value : undefined,
      class: classes || undefined,
      color: color.value || undefined,
      inset: model.value === 'inset' || undefined,
      vertical: model.value === 'vertical' || undefined,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-divider - misc subheaders

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-toolbar
      color="orange-lighten-1"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Message Board</v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list lines="two">
      <template v-for="(item, index) in items">
        <v-list-subheader
          v-if="item.header"
          :key="item.header"
          inset
        >
          {{ item.header }}
        </v-list-subheader>

        <v-divider
          v-else-if="item.divider"
          :key="index"
          inset
        ></v-divider>

        <v-list-item
          v-else
          :key="item.title"
          :prepend-avatar="item.avatar"
          ripple
        >
          <template v-slot:title>
            <div v-html="item.title"></div>
          </template>

          <template v-slot:subtitle>
            <div v-html="item.subtitle"></div>
          </template>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    {
      header: 'Today',
    },
    { divider: true },
    {
      avatar: 'https://picsum.photos/250/300?image=660',
      title: 'Meeting @ Noon',
      subtitle: `<span class="font-weight-bold">Spike Lee</span> &mdash; I'll be in your neighborhood`,
    },
    {
      avatar: 'https://picsum.photos/250/300?image=821',
      title: 'Summer BBQ <span class="text-grey-lighten-1"></span>',
      subtitle: '<span class="font-weight-bold">to Operations support</span> &mdash; Wish I could come.',
    },
    {
      avatar: 'https://picsum.photos/250/300?image=783',
      title: 'Yes yes',
      subtitle: '<span class="font-weight-bold">Bella</span> &mdash; Do you have Paris recommendations',
    },
    {
      header: 'Yesterday',
    },
    { divider: true },
    {
      avatar: 'https://picsum.photos/250/300?image=1006',
      title: 'Dinner tonight?',
      subtitle: '<span class="font-weight-bold">LaToya</span> &mdash; Do you want to hang out?',
    },
    {
      avatar: 'https://picsum.photos/250/300?image=146',
      title: 'So long',
      subtitle: '<span class="font-weight-bold">Nancy</span> &mdash; Do you see what time it is?',
    },
    {
      header: 'Last Week',
    },
    { divider: true },
    {
      avatar: 'https://picsum.photos/250/300?image=1008',
      title: 'Breakfast?',
      subtitle: '<span class="font-weight-bold">LaToya</span> &mdash; Do you want to hang out?',
    },
    {
      avatar: 'https://picsum.photos/250/300?image=839',
      title: 'Winter Porridge <span class="text-grey-lighten-1"></span>',
      subtitle: '<span class="font-weight-bold">cc: Daniel</span> &mdash; Tell me more...',
    },
    {
      avatar: 'https://picsum.photos/250/300?image=145',
      title: 'Oui oui',
      subtitle: '<span class="font-weight-bold">Nancy</span> &mdash; Do you see what time it is?',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          header: 'Today',
        },
        { divider: true },
        {
          avatar: 'https://picsum.photos/250/300?image=660',
          title: 'Meeting @ Noon',
          subtitle: `<span class="font-weight-bold">Spike Lee</span> &mdash; I'll be in your neighborhood`,
        },
        {
          avatar: 'https://picsum.photos/250/300?image=821',
          title: 'Summer BBQ <span class="text-grey-lighten-1"></span>',
          subtitle: '<span class="font-weight-bold">to Operations support</span> &mdash; Wish I could come.',
        },
        {
          avatar: 'https://picsum.photos/250/300?image=783',
          title: 'Yes yes',
          subtitle: '<span class="font-weight-bold">Bella</span> &mdash; Do you have Paris recommendations',
        },
        {
          header: 'Yesterday',
        },
        { divider: true },
        {
          avatar: 'https://picsum.photos/250/300?image=1006',
          title: 'Dinner tonight?',
          subtitle: '<span class="font-weight-bold">LaToya</span> &mdash; Do you want to hang out?',
        },
        {
          avatar: 'https://picsum.photos/250/300?image=146',
          title: 'So long',
          subtitle: '<span class="font-weight-bold">Nancy</span> &mdash; Do you see what time it is?',
        },
        {
          header: 'Last Week',
        },
        { divider: true },
        {
          avatar: 'https://picsum.photos/250/300?image=1008',
          title: 'Breakfast?',
          subtitle: '<span class="font-weight-bold">LaToya</span> &mdash; Do you want to hang out?',
        },
        {
          avatar: 'https://picsum.photos/250/300?image=839',
          title: 'Winter Porridge <span class="text-grey-lighten-1"></span>',
          subtitle: '<span class="font-weight-bold">cc: Daniel</span> &mdash; Tell me more...',
        },
        {
          avatar: 'https://picsum.photos/250/300?image=145',
          title: 'Oui oui',
          subtitle: '<span class="font-weight-bold">Nancy</span> &mdash; Do you see what time it is?',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-divider - misc portrait view

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-card-item class="bg-cyan-darken-1">
      <v-card-title>
        <span class="text-h5">Sarah Mcbeal</span>
      </v-card-title>

      <template v-slot:append>
        <v-defaults-provider
          :defaults="{
            VBtn: {
              variant: 'text',
              density: 'comfortable',
            }
          }"
        >
          <v-btn icon="mdi-chevron-left"></v-btn>

          <v-btn icon="mdi-pencil"></v-btn>

          <v-btn icon="mdi-dots-vertical"></v-btn>
        </v-defaults-provider>
      </template>
    </v-card-item>

    <v-list>
      <v-list-item
        append-icon="mdi-message-text"
        prepend-icon="mdi-phone"
        title="(650) 555-1234"
      ></v-list-item>

      <v-divider inset></v-divider>

      <v-list-item
        append-icon="mdi-message-text"
        prepend-icon="mdi-phone"
        title="(323) 555-6789"
      ></v-list-item>

      <v-divider inset></v-divider>

      <v-list-item
        prepend-icon="mdi-email"
        title="mcbeal@example.com"
      ></v-list-item>

      <v-divider inset></v-divider>

      <v-list-item
        prepend-icon="mdi-map-marker"
        title="Orlando, FL 79938"
      ></v-list-item>
    </v-list>

    <v-img
      height="200"
      src="https://picsum.photos/700?image=996"
      cover
    ></v-img>
  </v-card>
</template>

```

# Vuetify component v-divider - prop inset

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="425"
  >
    <v-list lines="two">
      <v-list-subheader>Today</v-list-subheader>

      <v-list-item
        prepend-avatar="https://cdn.vuetifyjs.com/images/lists/1.jpg"
        title="Brunch this weekend?"
      >
        <template v-slot:subtitle>
          <span class="font-weight-bold">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item
        prepend-avatar="https://cdn.vuetifyjs.com/images/lists/2.jpg"
      >
        <template v-slot:title>
          Summer BBQ <span class="text-grey-lighten-1">4</span>
        </template>

        <template v-slot:subtitle>
          <span class="font-weight-bold">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item
        prepend-avatar="https://cdn.vuetifyjs.com/images/lists/3.jpg"
        title="Oui oui"
      >
        <template v-slot:subtitle>
          <span class="font-weight-bold">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

```

# Vuetify component v-divider - prop vertical

Example code

```vue
<template>
  <div class="text-body-2 mb-1">dividers with <v-code>vertical</v-code></div>
  <v-toolbar color="purple">
    <template v-slot:prepend>
      <div class="text-h5 px-3">Title</div>
    </template>

    <v-divider class="mx-3" vertical></v-divider>
    <v-toolbar-title>My Home</v-toolbar-title>

    <v-toolbar-items>
      <v-btn variant="text">News</v-btn>
      <v-divider vertical></v-divider>
      <v-btn variant="text">Blog</v-btn>
      <v-divider vertical></v-divider>
      <v-btn variant="text">Music</v-btn>
    </v-toolbar-items>
    <v-divider vertical></v-divider>
    <v-app-bar-nav-icon class="ms-2"></v-app-bar-nav-icon>
  </v-toolbar>

  <div class="text-body-2 mt-3 mb-1">dividers with <v-code>vertical</v-code> and <v-code>inset</v-code></div>
  <v-toolbar color="teal">
    <template v-slot:prepend>
      <div class="text-h5 px-3">Title</div>
    </template>

    <v-divider class="mx-3" inset vertical></v-divider>
    <v-toolbar-title>My Home</v-toolbar-title>

    <v-toolbar-items>
      <v-btn variant="text">News</v-btn>
      <v-divider inset vertical></v-divider>
      <v-btn variant="text">Blog</v-btn>
      <v-divider inset vertical></v-divider>
      <v-btn variant="text">Music</v-btn>
    </v-toolbar-items>
    <v-divider inset vertical></v-divider>
    <v-app-bar-nav-icon class="ms-2"></v-app-bar-nav-icon>
  </v-toolbar>
</template>

```
