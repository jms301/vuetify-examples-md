# Vuetify component v-avatar - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :options="options"
    name="v-avatar"
  >
    <div class="text-center">
      <v-avatar
        v-bind="props"
        :image="image ? 'https://cdn.vuetifyjs.com/images/john-smirk.png' : undefined"
      ></v-avatar>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="icon" label="Icon"></v-checkbox>

      <v-checkbox v-model="image" label="Image"></v-checkbox>

      <v-slider
        v-model="size"
        label="Size"
        max="80"
        min="40"
        step="1"
      ></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const model = ref('default')
  const icon = ref(false)
  const image = ref(false)
  const size = ref(40)
  const options = ['tile']
  const props = computed(() => {
    return {
      color: !image.value && !icon.value ? 'surface-variant' : undefined,
      icon: icon.value ? '$vuetify' : undefined,
      image: image.value ? 'smirk.png' : undefined,
      rounded: model.value === 'tile' ? '0' : undefined,
      size: size.value === 40 ? undefined : `${size.value}`,
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<v-avatar${propsToString(props.value)}>${slots.value}</v-avatar>`
  })
</script>

```

# Vuetify component v-avatar - prop size

Example code

```vue
<template>
  <div class="d-flex align-center justify-space-around">
    <v-avatar color="primary" size="x-small">
      32
    </v-avatar>

    <v-avatar color="secondary">
      48
    </v-avatar>

    <v-avatar color="info" size="x-large">
      64
    </v-avatar>
  </div>
</template>

```

# Vuetify component v-avatar - slot default

Example code

```vue
<template>
  <div class="d-flex align-center justify-space-around">
    <v-avatar color="info">
      <v-icon icon="mdi-account-circle"></v-icon>
    </v-avatar>

    <v-avatar>
      <v-img
        alt="John"
        src="https://cdn.vuetifyjs.com/images/john.jpg"
      ></v-img>
    </v-avatar>

    <v-avatar color="red">
      <span class="text-h5">CJ</span>
    </v-avatar>
  </div>
</template>

```

# Vuetify component v-avatar - prop tile

Example code

```vue
<template>
  <div class="text-center">
    <v-avatar
      color="blue-darken-2"
      rounded="0"
    >
      <v-icon icon="mdi-alarm"></v-icon>
    </v-avatar>
  </div>
</template>

```

# Vuetify component v-avatar - misc profile card

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="434"
    rounded="0"
  >
    <v-img
      height="100%"
      src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
      cover
    >
      <v-avatar
        color="grey"
        rounded="0"
        size="150"
      >
        <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg" cover></v-img>
      </v-avatar>
      <v-list-item
        class="text-white"
        subtitle="Network Engineer"
        title="Marcus Obrien"
      ></v-list-item>
    </v-img>
  </v-card>
</template>

```

# Vuetify component v-avatar - misc avatar menu

Example code

```vue
<template>
  <v-container
    style="height: 300px"
    fluid
  >
    <v-row justify="center">
      <v-menu min-width="200px">
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            v-bind="props"
          >
            <v-avatar
              color="brown"
              size="large"
            >
              <span class="text-h5">{{ user.initials }}</span>
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-card-text>
            <div class="mx-auto text-center">
              <v-avatar
                color="brown"
              >
                <span class="text-h5">{{ user.initials }}</span>
              </v-avatar>
              <h3>{{ user.fullName }}</h3>
              <p class="text-caption mt-1">
                {{ user.email }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn
                variant="text"
                rounded
              >
                Edit Account
              </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn
                variant="text"
                rounded
              >
                Disconnect
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-menu>
    </v-row>
  </v-container>
</template>

<script setup>
  const user = {
    initials: 'JD',
    fullName: 'John Doe',
    email: 'john.doe@doe.com',
  }
</script>

<script>
  export default {
    data: () => ({
      user: {
        initials: 'JD',
        fullName: 'John Doe',
        email: 'john.doe@doe.com',
      },
    }),
  }
</script>

```

# Vuetify component v-avatar - misc advanced

Example code

```vue
<template>
  <v-expansion-panels class="pa-4" variant="popout">
    <v-expansion-panel
      v-for="(message, i) in messages"
      :key="i"
      hide-actions
    >
      <v-expansion-panel-title>
        <v-row
          align="center"
          class="spacer"
          no-gutters
        >
          <v-col
            cols="4"
            md="1"
            sm="2"
          >
            <v-avatar
              size="36px"
            >
              <v-img
                v-if="message.avatar"
                alt="Avatar"
                src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
              ></v-img>
              <v-icon
                v-else
                :color="message.color"
                :icon="message.icon"
              ></v-icon>
            </v-avatar>
          </v-col>

          <v-col
            class="hidden-xs text-left ms-2"
            md="3"
            sm="5"
          >
            <strong v-html="message.name"></strong>
            <span
              v-if="message.total"
              class="text-grey"
            >
              &nbsp;({{ message.total }})
            </span>
          </v-col>

          <v-col
            class="text-no-wrap text-left"
            cols="5"
            sm="3"
          >
            <v-chip
              v-if="message.new"
              :color="`${message.color}-lighten-1`"
              class="ms-0 me-2"
              size="small"
              label
            >
              {{ message.new }} new
            </v-chip>
            <strong v-html="message.title"></strong>
          </v-col>

          <v-col
            v-if="message.excerpt"
            class="text-medium-emphasis text-truncate hidden-sm-and-down"
          >
            &mdash;
            {{ message.excerpt }}
          </v-col>
        </v-row>
      </v-expansion-panel-title>

      <v-expansion-panel-text>
        <v-card-text v-text="lorem"></v-card-text>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script setup>
  const messages = [
    {
      avatar: 'https://avatars0.githubusercontent.com/u/9064066?v=4&s=460',
      name: 'John Leider',
      title: 'Welcome to Vuetify!',
      excerpt: 'Thank you for joining our community...',
    },
    {
      color: 'red',
      icon: 'mdi-account-multiple',
      name: 'Social',
      new: 1,
      total: 3,
      title: 'Twitter',
    },
    {
      color: 'teal',
      icon: 'mdi-tag',
      name: 'Promos',
      new: 2,
      total: 4,
      title: 'Shop your way',
      excerpt: 'New deals available, Join Today',
    },
  ]
  const lorem = 'Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos. Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no, nostro voluptaria sea eu. Suas eligendi ius at, at nemore equidem est. Sed in error hendrerit, in consul constituam cum.'
</script>

<script>
  export default {
    data: () => ({
      messages: [
        {
          avatar: 'https://avatars0.githubusercontent.com/u/9064066?v=4&s=460',
          name: 'John Leider',
          title: 'Welcome to Vuetify!',
          excerpt: 'Thank you for joining our community...',
        },
        {
          color: 'red',
          icon: 'mdi-account-multiple',
          name: 'Social',
          new: 1,
          total: 3,
          title: 'Twitter',
        },
        {
          color: 'teal',
          icon: 'mdi-tag',
          name: 'Promos',
          new: 2,
          total: 4,
          title: 'Shop your way',
          excerpt: 'New deals available, Join Today',
        },
      ],
      lorem: 'Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos. Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no, nostro voluptaria sea eu. Suas eligendi ius at, at nemore equidem est. Sed in error hendrerit, in consul constituam cum.',
    }),
  }
</script>

```
