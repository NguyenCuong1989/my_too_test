import admin from 'firebase-admin';

process.env.FIRESTORE_EMULATOR_HOST = 'localhost:8080';

admin.initializeApp({
  projectId: 'gen-lang-client-0863690953'
});

const db = admin.firestore();

async function seed() {
  console.log("🌱 Seeding local emulator with Master Authority...");

  const testUser = {
    uid: "test-user-id",
    email: "test@sli.ai",
    billing: {
      plan: "pro",
      quota_remaining: 1000,
      status: "active"
    }
  };

  const masterUser = {
    uid: "master-alpha-prime-omega",
    email: "nguyencuong.2509@gmail.com",
    billing: {
      plan: "unlimited",
      quota_remaining: 999999,
      status: "active",
      role: "admin"
    }
  };

  await db.collection('users').doc(testUser.uid).set(testUser);
  await db.collection('users').doc(masterUser.uid).set(masterUser);
  console.log("✅ Seed complete: Master (nguyencuong.2509@gmail.com) activated with UNLIMITED quota.");
}

seed().catch(console.error);
