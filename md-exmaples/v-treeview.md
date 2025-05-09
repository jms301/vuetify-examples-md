# Vuetify component v-treeview - usage

Example code

```vue
<template>
  <v-treeview :items="items"></v-treeview>
</template>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop dense

Example code

```vue
<template>
  <v-treeview
    :items="items"
    density="compact"
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop activatable

Example code

```vue
<template>
  <v-treeview
    :items="items"
    item-value="id"
    activatable
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop rounded

Example code

```vue
<template>
  <v-treeview
    :items="items"
    activatable
    rounded
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - slot append and label

Example code

```vue
<template>
  <v-treeview
    v-model:opened="open"
    :items="items"
    density="compact"
    item-value="title"
    activatable
    open-on-click
  >
    <template v-slot:prepend="{ item, isOpen }">
      <v-icon v-if="!item.file" :icon="isOpen ? 'mdi-folder-open' : 'mdi-folder'"></v-icon>

      <v-icon v-else :icon="files[item.file]"></v-icon>
    </template>
  </v-treeview>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const open = shallowRef(['public'])
  const files = shallowRef({
    html: 'mdi-language-html5',
    js: 'mdi-nodejs',
    json: 'mdi-code-json',
    md: 'mdi-language-markdown',
    pdf: 'mdi-file-pdf-box',
    png: 'mdi-file-image',
    txt: 'mdi-file-document-outline',
    xls: 'mdi-file-excel',
  })

  const items = [
    {
      title: '.git',
    },
    {
      title: 'node_modules',
    },
    {
      title: 'public',
      children: [
        {
          title: 'static',
          children: [{
            title: 'logo.png',
            file: 'png',
          }],
        },
        {
          title: 'favicon.ico',
          file: 'png',
        },
        {
          title: 'index.html',
          file: 'html',
        },
      ],
    },
    {
      title: '.gitignore',
      file: 'txt',
    },
    {
      title: 'babel.config.js',
      file: 'js',
    },
    {
      title: 'package.json',
      file: 'json',
    },
    {
      title: 'README.md',
      file: 'md',
    },
    {
      title: 'vue.config.js',
      file: 'js',
    },
    {
      title: 'yarn.lock',
      file: 'txt',
    },
  ]
</script>

```

# Vuetify component v-treeview - slot title

Example code

```vue
<template>
  <v-treeview
    v-model="model"
    :items="items"
    :lines="false"
    collapse-icon="mdi-chevron-down"
    density="compact"
    expand-icon="mdi-chevron-right"
    select-strategy="leaf"
    fluid
    selectable
  >
    <template v-slot:title="{ item }">
      <span :class="['text-caption', model.includes(item.value) && 'text-decoration-line-through']">
        {{ item.title }}
      </span>
    </template>
  </v-treeview>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const items = Array.from({ length: 10 }, (_, i) => ({
    value: `${i}`,
    title: `Example item ${i + 1}`,
    children: Array.from({ length: 25 }, (_, j) => ({
      value: `${i}-${j}`,
      title: `Example child item ${j}`,
    })),
  }))

  const model = shallowRef([])
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 10 }, (_, i) => ({
        value: `${i}`,
        title: `Example item ${i + 1}`,
        children: Array.from({ length: 25 }, (_, j) => ({
          value: `${i}-${j}`,
          title: `Example child item ${j}`,
        })),
      })),
      model: [],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop hoverable

Example code

```vue
<template>
  <v-treeview
    :items="items"
    hoverable
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      name: 'Applications :',
      children: [
        { id: 2, name: 'Calendar : app' },
        { id: 3, name: 'Chrome : app' },
        { id: 4, name: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      name: 'Documents :',
      children: [
        {
          id: 6,
          name: 'vuetify :',
          children: [
            {
              id: 7,
              name: 'src :',
              children: [
                { id: 8, name: 'index : ts' },
                { id: 9, name: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          name: 'material2 :',
          children: [
            {
              id: 11,
              name: 'src :',
              children: [
                { id: 12, name: 'v-btn : ts' },
                { id: 13, name: 'v-card : ts' },
                { id: 14, name: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      name: 'Downloads :',
      children: [
        { id: 16, name: 'October : pdf' },
        { id: 17, name: 'November : pdf' },
        { id: 18, name: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      name: 'Videos :',
      children: [
        {
          id: 20,
          name: 'Tutorials :',
          children: [
            { id: 21, name: 'Basic layouts : mp4' },
            { id: 22, name: 'Advanced techniques : mp4' },
            { id: 23, name: 'All about app : dir' },
          ],
        },
        { id: 24, name: 'Intro : mov' },
        { id: 25, name: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          name: 'Applications :',
          children: [
            { id: 2, name: 'Calendar : app' },
            { id: 3, name: 'Chrome : app' },
            { id: 4, name: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          name: 'Documents :',
          children: [
            {
              id: 6,
              name: 'vuetify :',
              children: [
                {
                  id: 7,
                  name: 'src :',
                  children: [
                    { id: 8, name: 'index : ts' },
                    { id: 9, name: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              name: 'material2 :',
              children: [
                {
                  id: 11,
                  name: 'src :',
                  children: [
                    { id: 12, name: 'v-btn : ts' },
                    { id: 13, name: 'v-card : ts' },
                    { id: 14, name: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          name: 'Downloads :',
          children: [
            { id: 16, name: 'October : pdf' },
            { id: 17, name: 'November : pdf' },
            { id: 18, name: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          name: 'Videos :',
          children: [
            {
              id: 20,
              name: 'Tutorials :',
              children: [
                { id: 21, name: 'Basic layouts : mp4' },
                { id: 22, name: 'Advanced techniques : mp4' },
                { id: 23, name: 'All about app : dir' },
              ],
            },
            { id: 24, name: 'Intro : mov' },
            { id: 25, name: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - misc search and filter

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="500">
    <v-sheet class="pa-4" color="surface-variant">
      <v-text-field
        v-model="search"
        clear-icon="mdi-close-circle-outline"
        label="Search Company Directory"
        variant="solo"
        clearable
        flat
        hide-details
      ></v-text-field>

      <v-checkbox-btn
        v-model="caseSensitive"
        label="Case sensitive search"
      ></v-checkbox-btn>
    </v-sheet>

    <v-treeview
      v-model:opened="open"
      :custom-filter="filter"
      :items="items"
      :search="search"
      item-value="id"
      open-on-click
    >
      <template v-slot:prepend="{ item }">
        <v-icon
          v-if="item.children"
          :icon="`mdi-${item.id === 1 ? 'home-variant' : 'folder-network'}`"
        ></v-icon>
      </template>
    </v-treeview>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const items = [
    {
      id: 1,
      title: 'Vuetify Human Resources',
      children: [
        {
          id: 2,
          title: 'Core team',
          children: [
            {
              id: 201,
              title: 'John',
            },
            {
              id: 202,
              title: 'Kael',
            },
            {
              id: 203,
              title: 'Nekosaur',
            },
            {
              id: 204,
              title: 'Jacek',
            },
            {
              id: 205,
              title: 'Andrew',
            },
          ],
        },
        {
          id: 3,
          title: 'Administrators',
          children: [
            {
              id: 301,
              title: 'Blaine',
            },
            {
              id: 302,
              title: 'Yuchao',
            },
          ],
        },
        {
          id: 4,
          title: 'Contributors',
          children: [
            {
              id: 401,
              title: 'Phlow',
            },
            {
              id: 402,
              title: 'Brandon',
            },
            {
              id: 403,
              title: 'Sean',
            },
          ],
        },
      ],
    },
  ]

  const open = shallowRef([1, 2])
  const search = shallowRef(null)
  const caseSensitive = shallowRef(false)

  function filter (value, search, item) {
    return caseSensitive.value ? value.indexOf(search) > -1 : value.toLowerCase().indexOf(search.toLowerCase()) > -1
  }
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Vuetify Human Resources',
          children: [
            {
              id: 2,
              title: 'Core team',
              children: [
                { id: 201, title: 'John' },
                { id: 202, title: 'Kael' },
                { id: 203, title: 'Nekosaur' },
                { id: 204, title: 'Jacek' },
                { id: 205, title: 'Andrew' },
              ],
            },
            {
              id: 3,
              title: 'Administrators',
              children: [
                { id: 301, title: 'Blaine' },
                { id: 302, title: 'Yuchao' },
              ],
            },
            {
              id: 4,
              title: 'Contributors',
              children: [
                { id: 401, title: 'Phlow' },
                { id: 402, title: 'Brandon' },
                { id: 403, title: 'Sean' },
              ],
            },
          ],
        },
      ],
      open: [1, 2],
      search: null,
      caseSensitive: false,
    }),

    methods: {
      filter (value, search, item) {
        return this.caseSensitive ? value.indexOf(search) > -1 : value.toLowerCase().indexOf(search.toLowerCase()) > -1
      },
    },
  }
</script>

```

# Vuetify component v-treeview - prop open all

Example code

```vue
<template>
  <v-treeview
    :items="items"
    item-value="id"
    open-all
  ></v-treeview>
</template>

<script setup>
  const items = [
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop selection type

Example code

```vue
<template>
  <v-sheet border rounded>
    <v-container fluid>
      <v-select
        v-model="strategy"
        :items="['leaf', 'single-leaf', 'independent', 'single-independent', 'classic']"
        label="Selection type"
      ></v-select>

      <v-row>
        <v-col cols="12" md="6">
          <v-treeview
            v-model:selected="selected"
            :items="items"
            :select-strategy="strategy"
            item-value="id"
            return-object
            selectable
          ></v-treeview>
        </v-col>

        <v-divider vertical></v-divider>

        <v-col class="pa-6" cols="12" md="6">
          <template v-if="!selected.length">No nodes selected.</template>

          <template v-else>
            <div v-for="node in selected" :key="node.id">
              {{ node.title }}
            </div>
          </template>
        </v-col>
      </v-row>
    </v-container>
  </v-sheet>
</template>

<script setup>
  import { ref, shallowRef } from 'vue'

  const strategy = shallowRef('leaf')
  const selected = shallowRef([])
  const items = ref([
    {
      id: 1,
      title: 'Root',
      children: [
        { id: 2, title: 'Child #1' },
        { id: 3, title: 'Child #2' },
        {
          id: 4,
          title: 'Child #3',
          children: [
            { id: 5, title: 'Grandchild #1' },
            { id: 6, title: 'Grandchild #2' },
          ],
        },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      strategy: 'leaf',
      selected: [],
      items: [
        {
          id: 1,
          title: 'Root',
          children: [
            { id: 2, title: 'Child #1' },
            { id: 3, title: 'Child #2' },
            {
              id: 4,
              title: 'Child #3',
              children: [
                { id: 5, title: 'Grandchild #1' },
                { id: 6, title: 'Grandchild #2' },
              ],
            },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop item props

Example code

```vue
<template>
  <v-treeview
    :items="items"
    item-props
    selectable
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      title: 'Applications :',
      disabled: true,
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              disabled: true,
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf', disabled: true },
        { id: 17, title: 'November : pdf', disabled: true },
        { id: 18, title: 'Tutorial : html', disabled: true },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

```

# Vuetify component v-treeview - prop color

Example code

```vue
<template>
  <v-treeview
    :items="items"
    color="warning"
    item-value="id"
    activatable
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop selected color

Example code

```vue
<template>
  <v-treeview
    :items="items"
    selected-color="red"
    selectable
  ></v-treeview>
</template>

<script setup>
  const items = [
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - prop fluid

Example code

```vue
<template>
  <v-treeview
    :items="items"
    fluid
  ></v-treeview>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      title: 'Applications :',
      children: [
        { id: 2, title: 'Calendar : app' },
        { id: 3, title: 'Chrome : app' },
        { id: 4, title: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      title: 'Documents :',
      children: [
        {
          id: 6,
          title: 'vuetify :',
          children: [
            {
              id: 7,
              title: 'src :',
              children: [
                { id: 8, title: 'index : ts' },
                { id: 9, title: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          title: 'material2 :',
          children: [
            {
              id: 11,
              title: 'src :',
              children: [
                { id: 12, title: 'v-btn : ts' },
                { id: 13, title: 'v-card : ts' },
                { id: 14, title: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      title: 'Downloads :',
      children: [
        { id: 16, title: 'October : pdf' },
        { id: 17, title: 'November : pdf' },
        { id: 18, title: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      title: 'Videos :',
      children: [
        {
          id: 20,
          title: 'Tutorials :',
          children: [
            { id: 21, title: 'Basic layouts : mp4' },
            { id: 22, title: 'Advanced techniques : mp4' },
            { id: 23, title: 'All about app : dir' },
          ],
        },
        { id: 24, title: 'Intro : mov' },
        { id: 25, title: 'Conference introduction : avi' },
      ],
    },
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          title: 'Applications :',
          children: [
            { id: 2, title: 'Calendar : app' },
            { id: 3, title: 'Chrome : app' },
            { id: 4, title: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          title: 'Documents :',
          children: [
            {
              id: 6,
              title: 'vuetify :',
              children: [
                {
                  id: 7,
                  title: 'src :',
                  children: [
                    { id: 8, title: 'index : ts' },
                    { id: 9, title: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              title: 'material2 :',
              children: [
                {
                  id: 11,
                  title: 'src :',
                  children: [
                    { id: 12, title: 'v-btn : ts' },
                    { id: 13, title: 'v-card : ts' },
                    { id: 14, title: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          title: 'Downloads :',
          children: [
            { id: 16, title: 'October : pdf' },
            { id: 17, title: 'November : pdf' },
            { id: 18, title: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          title: 'Videos :',
          children: [
            {
              id: 20,
              title: 'Tutorials :',
              children: [
                { id: 21, title: 'Basic layouts : mp4' },
                { id: 22, title: 'Advanced techniques : mp4' },
                { id: 23, title: 'All about app : dir' },
              ],
            },
            { id: 24, title: 'Intro : mov' },
            { id: 25, title: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - playground

Example code

```vue
<template>
  <div>
    <v-row justify="space-around">
      <v-switch
        v-model="dense"
        label="Dense"
      ></v-switch>
      <v-switch
        v-model="selectable"
        label="Selectable"
      ></v-switch>
      <v-switch
        v-model="activatable"
        label="Activatable"
      ></v-switch>
      <v-switch
        v-model="hoverable"
        label="Hoverable"
      ></v-switch>
      <v-switch
        v-model="shaped"
        label="Shaped"
      ></v-switch>
      <v-switch
        v-model="rounded"
        label="Rounded"
      ></v-switch>
      <v-switch
        v-model="openOnClick"
        label="Open on any item click"
      ></v-switch>
      <v-col cols="12">
        <v-select
          v-model="selectedColor"
          :disabled="!selectable"
          :items="selectedColors"
          label="Selected checkbox color"
        ></v-select>
      </v-col>
      <v-col cols="12">
        <v-select
          v-model="color"
          :disabled="!activatable"
          :items="selectedColors"
          label="Active node color"
        ></v-select>
      </v-col>
    </v-row>

    <v-treeview
      :activatable="activatable"
      :color="color"
      :dense="dense"
      :hoverable="hoverable"
      :items="items"
      :open-on-click="openOnClick"
      :rounded="rounded"
      :selectable="selectable"
      :selected-color="selectedColor"
      :shaped="shaped"
    ></v-treeview>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref([
    {
      id: 1,
      name: 'Applications :',
      children: [
        { id: 2, name: 'Calendar : app' },
        { id: 3, name: 'Chrome : app' },
        { id: 4, name: 'Webstorm : app' },
      ],
    },
    {
      id: 5,
      name: 'Documents :',
      children: [
        {
          id: 6,
          name: 'vuetify :',
          children: [
            {
              id: 7,
              name: 'src :',
              children: [
                { id: 8, name: 'index : ts' },
                { id: 9, name: 'bootstrap : ts' },
              ],
            },
          ],
        },
        {
          id: 10,
          name: 'material2 :',
          children: [
            {
              id: 11,
              name: 'src :',
              children: [
                { id: 12, name: 'v-btn : ts' },
                { id: 13, name: 'v-card : ts' },
                { id: 14, name: 'v-window : ts' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 15,
      name: 'Downloads :',
      children: [
        { id: 16, name: 'October : pdf' },
        { id: 17, name: 'November : pdf' },
        { id: 18, name: 'Tutorial : html' },
      ],
    },
    {
      id: 19,
      name: 'Videos :',
      children: [
        {
          id: 20,
          name: 'Tutorials :',
          children: [
            { id: 21, name: 'Basic layouts : mp4' },
            { id: 22, name: 'Advanced techniques : mp4' },
            { id: 23, name: 'All about app : dir' },
          ],
        },
        { id: 24, name: 'Intro : mov' },
        { id: 25, name: 'Conference introduction : avi' },
      ],
    },
  ])
  const dense = ref(false)
  const selectable = ref(false)
  const activatable = ref(false)
  const hoverable = ref(false)
  const openOnClick = ref(false)
  const shaped = ref(false)
  const rounded = ref(false)
  const color = ref('primary')
  const selectedColor = ref('accent')
  const selectedColors = ref([
    'accent',
    'teal',
    'red',
    'success',
    'warning lighten-2',
  ])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          name: 'Applications :',
          children: [
            { id: 2, name: 'Calendar : app' },
            { id: 3, name: 'Chrome : app' },
            { id: 4, name: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          name: 'Documents :',
          children: [
            {
              id: 6,
              name: 'vuetify :',
              children: [
                {
                  id: 7,
                  name: 'src :',
                  children: [
                    { id: 8, name: 'index : ts' },
                    { id: 9, name: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              name: 'material2 :',
              children: [
                {
                  id: 11,
                  name: 'src :',
                  children: [
                    { id: 12, name: 'v-btn : ts' },
                    { id: 13, name: 'v-card : ts' },
                    { id: 14, name: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          name: 'Downloads :',
          children: [
            { id: 16, name: 'October : pdf' },
            { id: 17, name: 'November : pdf' },
            { id: 18, name: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          name: 'Videos :',
          children: [
            {
              id: 20,
              name: 'Tutorials :',
              children: [
                { id: 21, name: 'Basic layouts : mp4' },
                { id: 22, name: 'Advanced techniques : mp4' },
                { id: 23, name: 'All about app : dir' },
              ],
            },
            { id: 24, name: 'Intro : mov' },
            { id: 25, name: 'Conference introduction : avi' },
          ],
        },
      ],
      dense: false,
      selectable: false,
      activatable: false,
      hoverable: false,
      openOnClick: false,
      shaped: false,
      rounded: false,
      color: 'primary',
      selectedColor: 'accent',
      selectedColors: [
        'accent',
        'teal',
        'red',
        'success',
        'warning lighten-2',
      ],
    }),
  }
</script>

```

# Vuetify component v-treeview - misc selectable icons

Example code

```vue
<template>
  <v-card>
    <v-toolbar
      color="surface-light"
      density="compact"
      title="Local hotspots"
      flat
    ></v-toolbar>

    <v-row dense>
      <v-col class="d-flex align-center" cols="12" sm="6">
        <v-treeview
          v-model:selected="tree"
          :items="items"
          :load-children="load"
          class="flex-1-0"
          false-icon="mdi-bookmark-outline"
          indeterminate-icon="mdi-bookmark-minus"
          item-title="name"
          item-value="id"
          select-strategy="classic"
          true-icon="mdi-bookmark"
          return-object
          selectable
        ></v-treeview>
      </v-col>

      <v-divider :vertical="$vuetify.display.mdAndUp" class="my-md-3"></v-divider>

      <v-col cols="12" sm="6">
        <v-card-text>
          <div
            v-if="tree.length === 0"
            class="text-h6 font-weight-light text-grey pa-4 text-center"
          >
            Select your favorite breweries
          </div>

          <div class="d-flex flex-wrap ga-1">
            <v-scroll-x-transition group hide-on-leave>
              <v-chip
                v-for="selection in tree"
                :key="selection.id"
                :prepend-icon="getIcon()"
                :text="selection.name"
                color="grey"
                size="small"
                border
                closable
                label
                @click:close="onClickClose(selection)"
              ></v-chip>
            </v-scroll-x-transition>
          </div>
        </v-card-text>
      </v-col>
    </v-row>

    <v-divider></v-divider>

    <template v-slot:actions>
      <v-btn
        text="Reset"
        @click="tree = []"
      ></v-btn>

      <v-spacer></v-spacer>

      <v-btn
        append-icon="mdi-content-save"
        color="surface-light"
        text="Save"
        variant="flat"
        border
      ></v-btn>
    </template>
  </v-card>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const icons = [
    'mdi-beer',
    'mdi-glass-mug',
    'mdi-liquor',
    'mdi-glass-mug-variant',
  ]

  const breweries = ref([])
  const tree = ref([])
  const types = ref([])
  const items = ref([{
    id: 1,
    name: 'All Breweries',
    children: [],
  }])

  watch(breweries, val => {
    types.value = val.reduce((acc, cur) => {
      const type = cur.brewery_type
      if (!acc.includes(type)) acc.push(type)
      return acc
    }, []).sort()

    const children = types.value.map(type => ({
      id: type,
      name: getName(type),
      children: getChildren(type),
    }))
    const rootObj = items.value[0]
    rootObj.children = children
    items.value = [rootObj]
  })

  function load () {
    if (breweries.value.length) return

    return fetch('https://api.openbrewerydb.org/breweries').then(res => res.json()).then(data => (breweries.value = data)).catch(err => console.log(err))
  }

  function getChildren (type) {
    const _breweries = []
    for (const brewery of breweries.value) {
      if (brewery.brewery_type !== type) continue
      _breweries.push({
        ...brewery,
        name: getName(brewery.name),
      })
    }
    return _breweries.sort((a, b) => {
      return a.name > b.name ? 1 : -1
    })
  }

  function getIcon () {
    return icons[Math.floor(Math.random() * icons.length)]
  }

  function getName (name) {
    return `${name.charAt(0).toUpperCase()}${name.slice(1)}`
  }

  function onClickClose (selection) {
    tree.value = tree.value.filter(item => item.id !== selection.id)
  }
</script>

```

# Vuetify component v-treeview - prop load children

Example code

```vue
<template>
  <v-container fluid>
    <v-row justify="space-between" dense>
      <v-col cols="12" md="5">
        <v-treeview
          v-model:activated="active"
          v-model:opened="open"
          :items="items"
          :load-children="fetchUsers"
          density="compact"
          item-title="name"
          item-value="id"
          activatable
          border
          fluid
          open-on-click
          rounded
        >
          <template v-slot:prepend="{ item }">
            <v-icon v-if="!item.children" icon="mdi-account"></v-icon>
          </template>
        </v-treeview>
      </v-col>

      <v-col class="d-flex text-center" cols="12" md="7">
        <v-card
          class="text-h6 justify-center align-center flex-1-1 d-flex"
          color="surface-light"
          height="100%"
          flat
          rounded
        >
          <template v-slot:text>
            <div v-if="!selected" class="text-subtitle-1">Select a User</div>

            <template v-else>
              <v-avatar :image="`https://avataaars.io/${avatar}`" class="mb-2" size="88"></v-avatar>

              <h3 class="text-h5">{{ selected.name }}</h3>

              <div class="text-medium-emphasis">{{ selected.email }}</div>

              <div class="text-medium-emphasis font-weight-bold">{{ selected.username }}</div>

              <v-divider class="my-4"></v-divider>

              <v-text-field
                :model-value="selected.company.name"
                class="mx-auto mb-2"
                density="compact"
                max-width="250"
                prefix="Company:"
                variant="solo"
                flat
                hide-details
                readonly
              ></v-text-field>

              <v-text-field
                :model-value="selected.website"
                class="mx-auto mb-2"
                density="compact"
                max-width="250"
                prefix="Website:"
                variant="solo"
                flat
                hide-details
                readonly
              ></v-text-field>

              <v-text-field
                :model-value="selected.phone"
                class="mx-auto"
                density="compact"
                max-width="250"
                prefix="Phone:"
                variant="solo"
                flat
                hide-details
                readonly
              ></v-text-field>
            </template>
          </template>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { computed, ref, watch } from 'vue'

  const avatars = [
    '?accessoriesType=Blank&avatarStyle=Circle&clotheColor=PastelGreen&clotheType=ShirtScoopNeck&eyeType=Wink&eyebrowType=UnibrowNatural&facialHairColor=Black&facialHairType=MoustacheMagnum&hairColor=Platinum&mouthType=Concerned&skinColor=Tanned&topType=Turban',
    '?accessoriesType=Sunglasses&avatarStyle=Circle&clotheColor=Gray02&clotheType=ShirtScoopNeck&eyeType=EyeRoll&eyebrowType=RaisedExcited&facialHairColor=Red&facialHairType=BeardMagestic&hairColor=Red&hatColor=White&mouthType=Twinkle&skinColor=DarkBrown&topType=LongHairBun',
    '?accessoriesType=Prescription02&avatarStyle=Circle&clotheColor=Black&clotheType=ShirtVNeck&eyeType=Surprised&eyebrowType=Angry&facialHairColor=Blonde&facialHairType=Blank&hairColor=Blonde&hatColor=PastelOrange&mouthType=Smile&skinColor=Black&topType=LongHairNotTooLong',
    '?accessoriesType=Round&avatarStyle=Circle&clotheColor=PastelOrange&clotheType=Overall&eyeType=Close&eyebrowType=AngryNatural&facialHairColor=Blonde&facialHairType=Blank&graphicType=Pizza&hairColor=Black&hatColor=PastelBlue&mouthType=Serious&skinColor=Light&topType=LongHairBigHair',
    '?accessoriesType=Kurt&avatarStyle=Circle&clotheColor=Gray01&clotheType=BlazerShirt&eyeType=Surprised&eyebrowType=Default&facialHairColor=Red&facialHairType=Blank&graphicType=Selena&hairColor=Red&hatColor=Blue02&mouthType=Twinkle&skinColor=Pale&topType=LongHairCurly',
  ]

  const pause = ms => new Promise(resolve => setTimeout(resolve, ms))

  const active = ref([])
  const avatar = ref(null)
  const open = ref([])
  const users = ref([])

  const items = computed(() => [
    {
      name: 'Users',
      children: users.value,
      id: 'users',
    },
  ])

  const selected = computed(() => {
    if (!active.value.length) return undefined

    const id = active.value[0]

    return users.value.find(user => user.id === id)
  })

  watch(selected, () => {
    randomAvatar()
  })

  async function fetchUsers (item) {
    await pause(1500)

    return fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then(json => (item.children.push(...json)))
      .catch(err => console.warn(err))
  }

  function randomAvatar () {
    avatar.value = avatars[Math.floor(Math.random() * avatars.length)]
  }
</script>

<script>
  const avatars = [
    '?accessoriesType=Blank&avatarStyle=Circle&clotheColor=PastelGreen&clotheType=ShirtScoopNeck&eyeType=Wink&eyebrowType=UnibrowNatural&facialHairColor=Black&facialHairType=MoustacheMagnum&hairColor=Platinum&mouthType=Concerned&skinColor=Tanned&topType=Turban',
    '?accessoriesType=Sunglasses&avatarStyle=Circle&clotheColor=Gray02&clotheType=ShirtScoopNeck&eyeType=EyeRoll&eyebrowType=RaisedExcited&facialHairColor=Red&facialHairType=BeardMagestic&hairColor=Red&hatColor=White&mouthType=Twinkle&skinColor=DarkBrown&topType=LongHairBun',
    '?accessoriesType=Prescription02&avatarStyle=Circle&clotheColor=Black&clotheType=ShirtVNeck&eyeType=Surprised&eyebrowType=Angry&facialHairColor=Blonde&facialHairType=Blank&hairColor=Blonde&hatColor=PastelOrange&mouthType=Smile&skinColor=Black&topType=LongHairNotTooLong',
    '?accessoriesType=Round&avatarStyle=Circle&clotheColor=PastelOrange&clotheType=Overall&eyeType=Close&eyebrowType=AngryNatural&facialHairColor=Blonde&facialHairType=Blank&graphicType=Pizza&hairColor=Black&hatColor=PastelBlue&mouthType=Serious&skinColor=Light&topType=LongHairBigHair',
    '?accessoriesType=Kurt&avatarStyle=Circle&clotheColor=Gray01&clotheType=BlazerShirt&eyeType=Surprised&eyebrowType=Default&facialHairColor=Red&facialHairType=Blank&graphicType=Selena&hairColor=Red&hatColor=Blue02&mouthType=Twinkle&skinColor=Pale&topType=LongHairCurly',
  ]

  const pause = ms => new Promise(resolve => setTimeout(resolve, ms))

  export default {
    data: () => ({
      active: [],
      avatar: null,
      open: [],
      users: [],
    }),

    computed: {
      items () {
        return [
          {
            name: 'Users',
            children: this.users,
          },
        ]
      },
      selected () {
        if (!this.active.length) return undefined

        const id = this.active[0]

        return this.users.find(user => user.id === id)
      },
    },

    watch: {
      selected: 'randomAvatar',
    },

    methods: {
      async fetchUsers (item) {
        // Remove in 6 months and say
        // you've made optimizations! :)
        await pause(1500)

        return fetch('https://jsonplaceholder.typicode.com/users')
          .then(res => res.json())
          .then(json => (item.children.push(...json)))
          .catch(err => console.warn(err))
      },
      randomAvatar () {
        this.avatar = avatars[Math.floor(Math.random() * avatars.length)]
      },
    },
  }
</script>

```
