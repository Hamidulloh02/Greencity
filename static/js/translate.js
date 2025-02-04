// Tarjima ma'lumotlari
const translations = {
  "en": {
      "title": "Welcome",
      "description": "This is a simple multilingual website.",
      "learnMoreBtn": "Learn More"
  },
  "uz": {
      "title": "Xush kelibsiz",
      "description": "Bu oddiy ikki tilli veb-sayt.",
      "learnMoreBtn": "Batafsil"
  }
};

// Tilni almashtirish funksiyasi
function changeLanguage(lang) {
  document.getElementById("title").textContent = translations[lang].title;
  document.getElementById("description").textContent = translations[lang].description;
  document.getElementById("learnMoreBtn").textContent = translations[lang].learnMoreBtn;
}

// Select box orqali tilni o'zgartirish
document.getElementById("languageSwitcher").addEventListener("change", function() {
  changeLanguage(this.value);
});

// Sahifa yuklanganda, brauzerda saqlangan tilni yuklash
document.addEventListener("DOMContentLoaded", function() {
  const defaultLang = "en"; // Default til
  document.getElementById("languageSwitcher").value = defaultLang;
  changeLanguage(defaultLang);
});
