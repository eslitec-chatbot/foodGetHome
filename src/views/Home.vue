<template>
  <div>
    <div>
      <img v-if="!showPokemon" class="scan__img" @click="scan()" src="@/assets/開啟頁-02.jpg" />
      <Pokemons v-if="showPokemon"
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
      <!-- <div>{{traceCode}}</div>
      <div>{{cropInfo}}</div> -->
    </div>
  </div>
</template>

<script>
import * as apis from "@/apis";
import Pokemons from "@/components/Pokemons"

export default {
  name: "home",
  components: {
    Pokemons,
  },
  data: () => ({
    profile: {
      userId: "gg",
      displayName: "gg",
      pictureUrl: "",
      statusMessage: ""
    },
    traceCode: "traceCode",
    cropInfo: "作物資訊。。",
    pokemonsData: {
      name: "我是誰???",
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
    showPokemon: false
  }),
  methods: {
    openWindow() {
      this.$liff.openWindow({
        url: "https://developers.line.me/en/docs/liff/overview/"
      });
    },
    closeWindow() {
      this.$liff.closeWindow();
    },
    sendMessage() {
      this.$liff
        .sendMessages([
          {
            type: "text",
            text: "哈囉哈囉"
          },
          {
            type: "sticker",
            packageId: "2",
            stickerId: "144"
          }
        ])
        .then(function() {
          window.alert("Message sent");
        })
        .catch(function(error) {
          window.alert("Error sending message: " + error);
        });
    },
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
    async scan() {
      // this.$router.push({ name: 'pokemon', params: { traceCode: "1081104517023392" } })
      let _this = this;
      _this.traceCode = "開始掃描。。";

      this.$liff
        .scanCode()
        .then(result => {
          // e.g. result = { value: "Hello LIFF app!" }

          let url = new URL(result.value);
          let params = url.searchParams;
          for (let pair of params.entries()) {
            if (pair[0] === "EnTraceCode") {
              _this.traceCode = pair[1];
            } else if (pair[0] === "t") {
              _this.traceCode = pair[1];
            }
          }
          if (_this.traceCode === "開始掃描。。") {
            _this.traceCode = "掃描失敗！";
          } else {
            _this.getCrop();
            apis.updateUserCrop({
              lineId: _this.profile.userId,
              traceCode: _this.traceCode
            })
            this.showPokemon = true
          }
        })
        .catch(err => {
          console.log(err);
          _this.traceCode = "掃描失敗！";
        });
    },
  async getCrop() {
      this.cropInfo = `開始找作物。。${String(this.traceCode)}`;
      const result = await apis.getCrop({
        traceCode: String(this.traceCode)
      });
      const result2 = await apis.getUserCrops({
        lineId: this.profile.userId
      });
      // this.cropInfo = result;
      this.pokemonsData.name = result.name
      this.pokemonsData.rarity = result.rarity
      this.pokemonsData.type = result.type
      this.pokemonsData.imgScanned = result.imgOrigin
      this.pokemonsData.production = result.production
      this.pokemonsData.packageDate = result.packageDate
      this.pokemonsData.location = result.location
      this.pokemonsData.farmerChat = result.farmerChat
      this.pokemonsData.url = result.url

      for (let r in result2) {
        if (result2[r].traceCode === this.traceCode) {
          this.pokemonsData.scanNumber = result2[r].scanNumber
        }
      }
    },
    async updateUserCrop() {
      // await apis.updateUserCrop()
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
    }
  },
  async created() {
    return new Promise((resolve, reject) => {
      this.createUser().then(res => {
        resolve()
      })
    });
  }
};
</script>

<style lang="scss" scoped>
.scan__img {
  width: 100vw;
  // @include flex(space-around, center);
  img {
    position: absolute;
  }
}
</style>
