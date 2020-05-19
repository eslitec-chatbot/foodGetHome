<template>
  <div>
    <div class="pokemon__background">
      <img class="pokemon__background__img" alt="飽飽" src="@/assets/寶物圖底.jpg">
      <div class="pokemon__background__prop pokemon__background__name">{{name}}</div>
      <div class="pokemon__background__prop pokemon__background__white pokemon__background__rarity">{{rarity}}</div>
      <div class="pokemon__background__prop pokemon__background__white pokemon__background__scanNumber">{{scanNumber}}</div>
      <div class="pokemon__background__prop pokemon__background__white pokemon__background__coupon">1</div>
      <div class="pokemon__background__prop pokemon__background__red pokemon__background__production">{{production}}</div>
      <div class="pokemon__background__prop pokemon__background__red pokemon__background__packageDate">{{packageDate}}</div>
      <div class="pokemon__background__prop pokemon__background__red pokemon__background__location">{{location}}</div>
      <div class="pokemon__background__prop pokemon__background__farmerChat">{{farmerChat}}</div>
      <div class="pokemon__background__prop pokemon__background__red pokemon__background__type">{{type}}</div>
      <!-- <div class="pokemon__background__prop pokemon__background__traceCode">{{traceCode}}</div> -->
      <div class="pokemon__background__prop pokemon__background__farmer" @click="openNewWindow()"></div>
      <img class="pokemon__background__prop pokemon__background__scanimg" alt="img-scan" :src="imgScanned" />
    </div>
  </div>
</template>>

<script>
export default {
  props: {
    name: {
      type: String,
      default: "待公開",
    },
    rarity: {
      type: String,
      default: "10/10",
    },
    imgScanned: {
      type: String,
      default: "https://foodpokemno.s3-ap-northeast-1.amazonaws.com/%E6%9C%AA%E5%91%BD%E5%90%8D-1_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F+1.png",
    },
    production: {
      type: String,
      default: "旅人食通信 X 以力科技",
    },
    packageDate: {
      type: String,
      default: "9999/12/31",
    },
    location: {
      type: String,
      default: "台灣Ｎｏ．１",
    },
    farmerChat: {
      type: String,
      default: "透過參與食農合作黑客松，設計出讓消費者更了解產銷履歷為我們的宗旨",
    },
    type: {
      type: String,
      default: "神秘君",
    },
    // traceCode: {
    //   type: String,
    //   default: "1081104517023392",
    // },
    scanNumber: {
      type: String,
      default: "5",
    },
    url: {
      type: String,
      default: "http://www.google.com",
    }
  },
  methods: {
    openNewWindow() {
      this.$liff.openWindow({
        url: this.url
      });
    }
  },
  computed: {
    traceCode() {
      return this.$route.params.traceCode
    }
  },
  created() {
    console.log(">>>this.$route.params.traceCode", this.$route.params.traceCode)
    // return this.$route.params.traceCode
  }
}
</script>
<style lang="scss" scoped>
.pokemon__background {
  position: relative;
  width: 375px;
  height: 517px;
  &__img {
    width: 100vw;
  }

  &__prop {
    z-index: 1;
    position: absolute;
  }

  &__name {
    width: 100vw;
    top: 9vw;
    text-align: center;
    font-size: 40px;
    font-weight: 900;
    font-family: PingFangSC-Medium, sans-serif;
    color: #45828A;
  }

  &__red {
    color: #D37168;
  }
  &__white {
    color: #ffffff;
  }

  &__type {
    left: 8.5vw;
    top: 35vw;
    width: 64px;
    font-size: 21px;
    font-weight: bolder;
    text-align: center;
  }

  &__location {
    left: 66vw;
    top: 33vw;
    width: 30vw;
    height: 11vw;
    font-weight: 900;
    text-align: center;
    overflow: hidden;
    text-overflow : ellipsis;
  }

  &__packageDate {
    left: 3vw;
    top: 60vw;
    width: 29vw;
    height: 11vw;
    font-weight: 900;
  }

  &__scanimg {
    left: 26.7vw;
    top: 21.3vw;
    min-width: calc(100vw / 3);
    max-height: 45.3vw;
    min-height: 45.3vw;
  }

  &__production {
    left: 68vw;
    top: 58.7vw;
    width: 29.3vw;
    font-weight: bolder;
    text-align: center;
    overflow: hidden;
    text-overflow : ellipsis;
  }

  &__rarity {
    left: 48vw;
    top: 73.3vw;
    width: 29.3vw;
    height: 10.3vw;
    font-weight: 900;
    text-align: center;
    overflow: hidden;
    text-overflow : ellipsis;
  }

  &__scanNumber {
    left: 48vw;
    top: 80.5vw;
    width: 29.3vw;
    height: 10.7vw;
    font-weight: 900;
    text-align: center;
    overflow: hidden;
    text-overflow : ellipsis;
  }

  &__coupon {
    left: 48vw;
    top: 88vw;
    width: 29.3vw;
    height: 10.7vw;
    font-weight: 900;
    text-align: center;
    overflow: hidden;
    text-overflow : ellipsis;
  }

  &__farmerChat {
    left: 5.3vw;
    top: 107vw;
    width: 90vw;
    height: 10.7vw;
    font-size: 12px;
    font-weight: 500;
    text-align: left;
  }

  &__farmer {
    opacity: 0.1;
    border: 1px ;
    left: 28vw;
    top: 122vw;
    width: 45vw;
    height: 10.7vw;
  }
}
</style>