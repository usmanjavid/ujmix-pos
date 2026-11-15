# Simple cloud backups — Windows 0.4.1

**OneDrive is the default.** Proton Drive, Google Drive and Dropbox are also supported through their Windows sync applications. You do not need to register an application or enter client IDs in UJMix POS.

## Set up

1. Install your provider's Windows app and sign in to your own account there.
2. In UJMix POS, open Settings → Backup and select the provider. Select **Choose [provider] sync folder** and choose a folder inside its synced drive. For OneDrive, **Use detected OneDrive folder** is available when Windows exposes an existing OneDrive folder.
3. Keep that folder available offline in the provider's app. UJMix POS creates `UJMix POS Backups/uj-retail-scheduled.ujbak` there.
4. Set a backup password and keep it separately for recovery on another PC.
5. Choose Daily, Weekly or Monthly, or click Back up now. Automatic backups run while UJMix POS is open; missed schedules catch up on reopening.

Only choose an actual synced folder. Selecting an ordinary local folder will not upload it. The POS confirms the local encrypted copy; use the provider's app to confirm successful online syncing. Internet, available account storage and the running sync app are needed for uploads. Providers may change their free storage allowances.

Provider software: [OneDrive](https://www.microsoft.com/microsoft-365/onedrive/download), [Proton Drive](https://proton.me/drive/download), [Google Drive](https://www.google.com/drive/download/), [Dropbox](https://www.dropbox.com/install). Download and sign in yourself; the POS does not install these apps or read cloud account credentials.

## Restore

Make the desired `.ujbak` file available locally through your sync app. In Settings → Backup, choose **Restore from synced folder…** (opens your configured backup folder) or **Restore from file…**. Enter the file's original backup password, type RESTORE and select the file. A local safety copy is made before replacement; all users are signed out after restoration.

Changing the backup password affects future files only. Earlier files keep their original password. Without a backup password, recovery needs the original Windows profile's database key.

## Clear and upgrade

Clear saved backups removes managed UJMix POS files from the configured local and sync folders, after typing CLEAR. The provider may sync those deletions. Safety copies and manual backups saved elsewhere remain available.

Existing sync-folder selections and backup schedules are preserved on upgrade. Existing local-only selections remain local-only. Previous direct connections are no longer used; select a sync folder to resume cloud copies. No online files are deleted by this migration.
