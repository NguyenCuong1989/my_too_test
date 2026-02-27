import admin from 'firebase-admin';

process.env.FIRESTORE_EMULATOR_HOST = 'localhost:8080';

admin.initializeApp({
  projectId: 'gen-lang-client-0863690953'
});

const db = admin.firestore();

async function seed() {
  console.log("🌱 Seeding local emulator...");

  const testUser = {
    uid: "test-user-id",
    email: "test@sli.ai",
    billing: {
      plan: "pro",
      quota_remaining: 1000,
      status: "active"
    }
  };

  await db.collection('users').doc(testUser.uid).set(testUser);
  console.log("✅ Seed complete: test-user-id created with 1000 items quota.");
}

seed().catch(console.error);
