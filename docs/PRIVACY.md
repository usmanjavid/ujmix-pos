# UJMix POS data and privacy

Store records, account password hashes, unfinished invoices and customer details are stored in the local encrypted database. Windows Credential Manager protects local encryption material. Set a separate portable backup password for restoration on another PC, and store that password securely. Keep backups protected and verify restoration before relying on them.

Cloud backups use a folder selected by you in your own cloud provider's desktop app. That app handles sign-in and upload under its own terms; UJMix POS does not collect OAuth tokens. A successful local copy does not prove the provider has uploaded it.

Optional local AI runs on the PC. Instant insights and financial answers use approved local database queries. The desktop app does not automatically send shop data to ChatGPT, Claude or Gemini. Support links open the website or WhatsApp only when selected. Diagnostics are previewed before local saving and are not automatically transmitted.

A PC activation code is derived from a hashed Windows installation identifier (or a persistent local fallback). Customer license files contain the registered name, term, expiry and PC code. Share them only with the software owner/support as needed. Password recovery codes are one-use and should be kept securely outside the PC. Recovery through an older backup can restore older credentials; secure and retire old backup copies appropriately.

You control staff access, backup destinations, retention and any records shared with support. Closing the application does not delete records. Deactivating a license does not delete records.

Remember me stores a random sign-in token in Windows Credential Manager and its hash in the encrypted shop database; the password is not saved. Sign-out and idle expiry end remembered sign-in. Trial first-use and clock information is retained separately from shop backups and mirrored in Windows Credential Manager.
