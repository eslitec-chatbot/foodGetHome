<template>
  <div>
    <div class="poke__pokebackground" v-if="!showPokemon2">
      <img class="poke__pokebackground__img" alt="藏飽櫃" src="@/assets/藏飽櫃底圖.png">
      <!-- 1 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_1" alt="poke" :src="crops[0].scaned ? crops[0].imageUrl : crops[0].imageScan" @click="changeView(0)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_1__caption">{{crops[0].cropName}}</div>
      <!-- 2 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_2" alt="poke" :src="crops[1].scaned ? crops[1].imageUrl : crops[1].imageScan" @click="changeView(1)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_2__caption">{{crops[1].cropName}}</div>
      <!-- 3 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_3" alt="poke" :src="crops[2].scaned ? crops[2].imageUrl : crops[2].imageScan" @click="changeView(2)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_3__caption">{{crops[2].cropName}}</div>
      <!-- 4 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_4" alt="poke" :src="crops[3].scaned ? crops[3].imageUrl : crops[3].imageScan" @click="changeView(3)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_4__caption">{{crops[3].cropName}}</div>
      <!-- 5  -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_5" alt="poke" :src="crops[4].scaned ? crops[4].imageUrl : crops[4].imageScan" @click="changeView(4)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_5__caption">{{crops[4].cropName}}</div>
      <!-- 6 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_6" alt="poke" :src="crops[5].scaned ? crops[5].imageUrl : crops[5].imageScan" @click="changeView(5)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_6__caption">{{crops[5].cropName}}</div>
      <!-- 7 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_7" alt="poke" :src="crops[6].scaned ? crops[6].imageUrl : crops[6].imageScan" @click="changeView(6)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_7__caption">{{crops[6].cropName}}</div>
      <!-- 8 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_8" alt="poke" :src="crops[7].scaned ? crops[7].imageUrl : crops[7].imageScan" @click="changeView(7)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_8__caption">{{crops[7].cropName}}</div>
      <!-- 9 -->
      <img class="poke__pokebackground__img__poke poke__pokebackground__poke_9" alt="poke" :src="crops[8].scaned ? crops[8].imageUrl : crops[8].imageScan" @click="changeView(8)" />
      <div class="poke__pokebackground__poke_caption poke__pokebackground__poke_9__caption">{{crops[8].cropName}}</div>
    </div>
      <Pokemons v-if="showPokemon2"
        :name="pokemonsData.name"
        :rarity="pokemonsData.rarity"
        :imgScanned="pokemonsData.imgScanned"
        :production="pokemonsData.production"
        :packageDate="pokemonsData.packageDate"
        :location="pokemonsData.location"
        :farmerChat="pokemonsData.farmerChat"
        :type="pokemonsData.type"
        :scanNumber="pokemonsData.scanNumber"
        :url="pokemonsData.url"
      ></Pokemons>
  </div>
</template>

<script>
import * as apis from "@/apis";
import Pokemons from "@/components/Pokemons"

export default {
  name: "poke",
  components: {
    Pokemons,
  },
  data: () => ({
    showPokemon2: false,
    profile: {
      userId: "cc",
      displayName: "cc",
      pictureUrl: "",
      statusMessage: ""
    },
    traceCode: "111",
    poke: [],
    pokemonsData: {
      name: "我是誰",
      rarity: "???",
      imgScanned: "",
      production: "???",
      packageDate: "???",
      location: "台灣No.1",
      farmerChat: "工程師",
      type: "無",
      scanNumber: "",
      url: ""
    },
    crops: [
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
      {
        imageUrl: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        imageScan: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
        cropName: "？？？",
        scaned: false,
        traceCode: "",
        pokemonsData: {},
      },
    ]
  }),
  methods: {
    getProfile() {
      let _this = this;
      return new Promise((resolve, reject) => {
        this.$liff
          .getProfile()
          .then(profile => {
            _this.profile = profile;
            resolve(profile);
          })
          .catch(function(error) {
            console.log("Error getting profile: " + error);
            reject(error);
          });
      });
    },
    async createUser() {
      return new Promise((resolve, reject) => {
        this.getProfile()
          .then(() => {
            apis.createUser({
              lineId: this.profile.userId,
              name: this.profile.displayName,
              profileImage: this.profile.pictureUrl
            }).then(res => {
              resolve()
            }).catch((err) => reject(err))
          })
          .catch((err) => reject(err));
      })
    },
    changeView(index) {
      if (Object.keys(this.crops[index].pokemonsData).length > 0) {
        this.pokemonsData.name = this.crops[index].pokemonsData.name
        this.pokemonsData.rarity = this.crops[index].pokemonsData.rarity
        this.pokemonsData.imgScanned = this.crops[index].pokemonsData.imgOrigin
        this.pokemonsData.packageDate = this.crops[index].pokemonsData.packageDate
        this.pokemonsData.location = this.crops[index].pokemonsData.location
        this.pokemonsData.farmerChat = this.crops[index].pokemonsData.farmerChat
        this.pokemonsData.type = this.crops[index].pokemonsData.type
        this.pokemonsData.scanNumber = this.crops[index].pokemonsData.scanNumber
        this.pokemonsData.url = this.crops[index].pokemonsData.url
        this.pokemonsData.production = this.crops[index].pokemonsData.production
        this.showPokemon2 = true
      }
    }
  },
  created() {
    return new Promise((resolve, reject) => {
      this.createUser().then(res => {
        resolve()
      }).catch(e => reject())
    });
  },
  async mounted() {
    let dataCrops = await apis.getAllCrop();
    const result2 = await apis.getUserCrops({
      lineId: this.profile.userId
    });
    this.poke = result2;
    for (let c in dataCrops) {
      this.crops[c].imageUrl = dataCrops[c].imgScanned
      this.crops[c].imageScan = dataCrops[c].imgUnscanned
      this.crops[c].cropName = dataCrops[c].name
      this.crops[c].traceCode = dataCrops[c].traceCode
      for (let p in this.poke) {
        if (this.poke[p].traceCode === this.crops[c].traceCode) {
          this.crops[c].scaned = true;
          this.crops[c].pokemonsData = dataCrops[c];
          this.crops[c].pokemonsData.scanNumber = this.poke[p].scanNumber;
        }
      }
    }
  }
};
</script>
<style lang="scss" scoped>
.poke__pokebackground {
  width: 100vw;
  // @include flex(space-around, center);
  img {
    position: absolute;
  }
  &__img {
    width: 100%;
    z-index: 1;
    top: 0;
    left: 0;
  }

  &__img__poke {
    width: 95px !important;
    height: 95px;
  }

  &__poke_caption {
    width: 26.7vw;
    z-index: 101;
    position: absolute;
    white-space : nowrap;
    overflow: hidden;
    text-overflow : ellipsis;
  }

  &__poke_1 {
    z-index: 100;
    top: calc((138vw - 34.7vw) / 3);
    left: calc(6.7vw);
    &__caption {
      left: 6.7vw;
      top: calc((138vw - 34.7vw) / 3 + 100px);
    }
  }
  &__poke_2 {
    z-index: 100;
    top: calc((138vw - 34.7vw) / 3);
    left: calc(37.3vw);
    &__caption {
      left: calc(37.3vw);
      top: calc((138vw - 34.7vw) / 3 + 100px);
    }
  }
  &__poke_3 {
    z-index: 100;
    top: calc((138vw - 34.7vw) / 3);
    left: calc(68vw);
    &__caption {
      left: calc(68vw);
      top: calc((138vw - 34.7vw) / 3 + 100px);
    }
  }
  &__poke_4 {
    z-index: 100;
    top: calc((138vw - 34.7vw) * 2 / 3);
    left: calc(6.7vw);
    &__caption {
      left: calc(6.7vw);
      top: calc((138vw - 34.7vw) * 2 / 3 + 100px);
    }
  }
  &__poke_5 {
    z-index: 100;
    top: calc((138vw - 34.7vw) * 2 / 3);
    left: calc(37.3vw);
    &__caption {
      left: calc(37.3vw);
      top: calc((138vw - 34.7vw) * 2 / 3 + 100px);
    }
  }
  &__poke_6 {
    z-index: 100;
    top: calc((138vw - 34.7vw) * 2 / 3);
    left: calc(68vw);
    &__caption {
      left: calc(68vw);
      top: calc((138vw - 34.7vw) * 2 / 3 + 100px);
    }
  }
  &__poke_7 {
    z-index: 100;
    top: calc((138vw - 34.7vw));
    left: calc(25px);
    &__caption {
      left: calc(25px);
      top: calc((138vw - 34.7vw + 100px));
    }
  }
  &__poke_8 {
    z-index: 100;
    top: calc((138vw - 34.7vw));
    left: calc(37.3vw);
    &__caption {
      left: calc(37.3vw);
      top: calc((138vw - 34.7vw + 100px));
    }
  }
  &__poke_9 {
    z-index: 100;
    top: calc((138vw - 34.7vw));
    left: calc(68vw);
    &__caption {
      left: calc(68vw);
      top: calc((138vw - 34.7vw + 100px));
    }
  }
}
</style>