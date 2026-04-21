# API Comparison Report

| Item | v1 | v2 |
|------|----|----|
| Base Path | `/api/v1` | `/api/v2` |
## Summary: Added=314, Removed=115, Modified=40


## Summary: Added=314, Removed=115, Modified=... (see below)

## Added APIs (314)

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/ai/agents` | Create Agent |
| `POST` | `/ai/agents/accounts` | Create Agent account |
| `POST` | `/ai/agents/accounts/delete` | Delete Agent account |
| `POST` | `/ai/agents/accounts/models` | List Agent account models |
| `POST` | `/ai/agents/accounts/models/create` | Create Agent account model |
| `POST` | `/ai/agents/accounts/models/delete` | Delete Agent account model |
| `POST` | `/ai/agents/accounts/models/update` | Update Agent account model |
| `POST` | `/ai/agents/accounts/search` | Page Agent accounts |
| `POST` | `/ai/agents/accounts/update` | Update Agent account |
| `POST` | `/ai/agents/accounts/verify` | Verify Agent account |
| `POST` | `/ai/agents/agent/bind` | Bind Agent role channel |
| `POST` | `/ai/agents/agent/channels` | Get Agent role channels from config file |
| `POST` | `/ai/agents/agent/create` | Create Agent role |
| `POST` | `/ai/agents/agent/delete` | Delete Agent role |
| `POST` | `/ai/agents/agent/list` | Get configured Agent roles from config file |
| `POST` | `/ai/agents/agent/md/list` | Get Agent role markdown files |
| `POST` | `/ai/agents/agent/md/update` | Update Agent role markdown file |
| `POST` | `/ai/agents/agent/unbind` | Unbind Agent role channel |
| `POST` | `/ai/agents/channel/dingtalk/get` | Get Agent DingTalk channel config |
| `POST` | `/ai/agents/channel/dingtalk/update` | Update Agent DingTalk channel config |
| `POST` | `/ai/agents/channel/discord/get` | Get Agent Discord channel config |
| `POST` | `/ai/agents/channel/discord/update` | Update Agent Discord channel config |
| `POST` | `/ai/agents/channel/feishu/get` | Get Agent Feishu channel config |
| `POST` | `/ai/agents/channel/feishu/update` | Update Agent Feishu channel config |
| `POST` | `/ai/agents/channel/pairing/approve` | Approve Agent channel pairing code |
| `POST` | `/ai/agents/channel/qqbot/get` | Get Agent QQ Bot channel config |
| `POST` | `/ai/agents/channel/qqbot/update` | Update Agent QQ Bot channel config |
| `POST` | `/ai/agents/channel/telegram/get` | Get Agent Telegram channel config |
| `POST` | `/ai/agents/channel/telegram/update` | Update Agent Telegram channel config |
| `POST` | `/ai/agents/channel/wecom/get` | Get Agent QQ Bot channel config |
| `POST` | `/ai/agents/channel/wecom/update` | Update Agent WeCom channel config |
| `POST` | `/ai/agents/channel/weixin/login` | Login Agent Weixin channel |
| `POST` | `/ai/agents/config-file/get` | Get Agent config file |
| `POST` | `/ai/agents/config-file/update` | Update Agent config file |
| `POST` | `/ai/agents/delete` | Delete Agent |
| `POST` | `/ai/agents/model/get` | Get Agent model config |
| `POST` | `/ai/agents/model/update` | Update Agent model config |
| `POST` | `/ai/agents/other/get` | Get Agent Other config |
| `POST` | `/ai/agents/other/update` | Update Agent Other config |
| `POST` | `/ai/agents/overview` | Get Agent overview |
| `POST` | `/ai/agents/plugin/check` | Check Agent plugin installation status |
| `POST` | `/ai/agents/plugin/install` | Install Agent plugin |
| `POST` | `/ai/agents/plugin/uninstall` | Uninstall Agent plugin |
| `POST` | `/ai/agents/plugin/upgrade` | Upgrade Agent plugin |
| `GET` | `/ai/agents/providers` | Get Providers |
| `POST` | `/ai/agents/remark` | Update Agent remark |
| `POST` | `/ai/agents/search` | Page Agents |
| `POST` | `/ai/agents/security/get` | Get Agent Security config |
| `POST` | `/ai/agents/security/update` | Update Agent Security config |
| `POST` | `/ai/agents/skills/install` | Install Agent skill |
| `POST` | `/ai/agents/skills/list` | List Agent skills |
| `POST` | `/ai/agents/skills/search` | Search Agent skills |
| `POST` | `/ai/agents/skills/update` | Update Agent skill status |
| `POST` | `/ai/agents/token/reset` | Reset Agent token |
| `POST` | `/ai/agents/website/bind` | Bind Agent website |
| `POST` | `/ai/mcp/domain/bind` | Bind Domain for mcp server |
| `GET` | `/ai/mcp/domain/get` | Get bin Domain for mcp server |
| `POST` | `/ai/mcp/domain/update` | Update bind Domain for mcp server |
| `POST` | `/ai/mcp/search` | List mcp servers |
| `POST` | `/ai/mcp/server` | Create mcp server |
| `POST` | `/ai/mcp/server/del` | Delete mcp server |
| `POST` | `/ai/mcp/server/op` | Operate mcp server |
| `POST` | `/ai/mcp/server/update` | Update mcp server |
| `POST` | `/ai/ollama/close` | Close Ollama model conn |
| `GET` | `/apps/:key` | Search app by key |
| `GET` | `/apps/detail/:appId/:version/:type` | Search app detail by appid |
| `GET` | `/apps/detail/node/:appKey/:version` | Search app detail by appkey and version |
| `GET` | `/apps/details/:id` | Get app detail by id |
| `GET` | `/apps/icon/:key` | Get app icon by app_id |
| `POST` | `/apps/ignored/cancel` | Cancel Ignore Upgrade App |
| `GET` | `/apps/ignored/detail` | List Upgrade Ignored App |
| `POST` | `/apps/installed/config/update` | Update app config |
| `POST` | `/apps/installed/conninfo` | Search app password by key |
| `GET` | `/apps/installed/delete/check/:appInstallId` | Check before delete |
| `GET` | `/apps/installed/info/:appInstallId` | Get app install info |
| `GET` | `/apps/installed/params/:appInstallId` | Search params by appInstallId |
| `GET` | `/apps/services/:key` | Search app service by key |
| `POST` | `/apps/sync/local` | Sync local  app list |
| `POST` | `/apps/sync/remote` | Sync remote app list |
| `POST` | `/backups` | Create backup account |
| `POST` | `/backups/backup` | Backup system data |
| `POST` | `/backups/buckets` | List buckets |
| `POST` | `/backups/check` | Check backup account |
| `POST` | `/backups/del` | Delete backup account |
| `GET` | `/backups/local` | get local backup dir |
| `GET` | `/backups/options` | Load backup account options |
| `POST` | `/backups/record/del` | Delete backup record |
| `POST` | `/backups/record/description/update` | Update backup record description |
| `POST` | `/backups/record/download` | Download backup record |
| `POST` | `/backups/record/search` | Page backup records |
| `POST` | `/backups/record/search/bycronjob` | Page backup records by cronjob |
| `POST` | `/backups/record/size` | Load backup record size |
| `POST` | `/backups/recover` | Recover system data |
| `POST` | `/backups/recover/byupload` | Recover system data by upload |
| `POST` | `/backups/refresh/token` | Refresh token |
| `POST` | `/backups/search` | Search backup accounts with page |
| `POST` | `/backups/search/files` | List files from backup accounts |
| `POST` | `/backups/update` | Update backup account |
| `POST` | `/backups/upload` | Upload file for recover |
| `POST` | `/containers/compose/clean/log` | Clean compose log |
| `POST` | `/containers/compose/env` | Load compose environment variables |
| `POST` | `/containers/files/content` | Get container file content |
| `POST` | `/containers/files/del` | Delete container file |
| `POST` | `/containers/files/download` | Download container file |
| `POST` | `/containers/files/search` | List container files |
| `POST` | `/containers/files/size` | Get container file size |
| `POST` | `/containers/files/upload` | Upload container file |
| `POST` | `/containers/item/stats` | Load container stats size |
| `POST` | `/containers/list/byimage` | List containers by image |
| `POST` | `/containers/repo/status` | Load repo status |
| `GET` | `/containers/search/log` | Container logs |
| `GET` | `/containers/stats/:id` | Container stats |
| `GET` | `/containers/status` | Load containers status |
| `POST` | `/containers/template/batch` | Bacth compose template |
| `POST` | `/containers/users` | Load container users |
| `GET` | `/core/auth/captcha` | Load captcha |
| `POST` | `/core/auth/login` | User login |
| `POST` | `/core/auth/logout` | User logout |
| `POST` | `/core/auth/mfalogin` | User login with mfa |
| `POST` | `/core/auth/passkey/begin` | User login with passkey |
| `POST` | `/core/auth/passkey/finish` | User login with passkey |
| `GET` | `/core/auth/setting` | Get Setting For Login |
| `POST` | `/core/backups` | Create backup account |
| `GET` | `/core/backups/client/:clientType` | Load backup account base info |
| `POST` | `/core/backups/del` | Delete backup account |
| `POST` | `/core/backups/refresh/token` | Refresh token |
| `POST` | `/core/backups/update` | Update backup account |
| `POST` | `/core/commands` | Create command |
| `GET` | `/core/commands/command` | List commands |
| `POST` | `/core/commands/del` | Delete command |
| `POST` | `/core/commands/export` | Export command |
| `POST` | `/core/commands/import` | Import command |
| `POST` | `/core/commands/search` | Page commands |
| `GET` | `/core/commands/tree` | Tree commands |
| `POST` | `/core/commands/update` | Update command |
| `POST` | `/core/groups` | Create group |
| `POST` | `/core/groups/del` | Delete group |
| `POST` | `/core/groups/search` | List groups |
| `POST` | `/core/groups/update` | Update group |
| `POST` | `/core/logs/clean` | Clean operation logs |
| `POST` | `/core/logs/login` | Page login logs |
| `POST` | `/core/logs/operation` | Page operation logs |
| `POST` | `/core/script` | Add script |
| `POST` | `/core/script/del` | Delete script |
| `POST` | `/core/script/search` | Page script |
| `POST` | `/core/script/sync` | Sync script from remote |
| `POST` | `/core/script/update` | Update script |
| `POST` | `/core/settings/api/config/generate/key` | generate api key |
| `POST` | `/core/settings/api/config/update` | Update api config |
| `GET` | `/core/settings/apps/store/config` | Get appstore config |
| `POST` | `/core/settings/apps/store/update` | Update appstore config |
| `POST` | `/core/settings/bind/update` | Update system bind info |
| `POST` | `/core/settings/by` | Load system setting by key |
| `POST` | `/core/settings/expired/handle` | Reset system password expired |
| `GET` | `/core/settings/interface` | Load system address |
| `GET` | `/core/settings/memo` | Load dashboard memo |
| `POST` | `/core/settings/memo` | Update dashboard memo |
| `POST` | `/core/settings/menu/default` | Default menu |
| `POST` | `/core/settings/menu/update` | Update system setting |
| `POST` | `/core/settings/mfa` | Load mfa info |
| `POST` | `/core/settings/mfa/bind` | Bind mfa |
| `GET` | `/core/settings/passkey/list` | List passkeys |
| `POST` | `/core/settings/passkey/register/begin` | Begin passkey registration |
| `POST` | `/core/settings/passkey/register/finish` | Finish passkey registration |
| `DELETE` | `/core/settings/passkey/{id}` | Delete passkey |
| `POST` | `/core/settings/password/update` | Update system password |
| `POST` | `/core/settings/port/update` | Update system port |
| `POST` | `/core/settings/proxy/update` | Update proxy setting |
| `POST` | `/core/settings/search` | Load system setting info |
| `GET` | `/core/settings/search/available` | Load system available status |
| `POST` | `/core/settings/ssl/download` | Download system cert |
| `GET` | `/core/settings/ssl/info` | Load system cert info |
| `POST` | `/core/settings/ssl/update` | Update system ssl |
| `POST` | `/core/settings/terminal/search` | Load system terminal setting info |
| `POST` | `/core/settings/terminal/update` | Update system terminal setting |
| `POST` | `/core/settings/update` | Update system setting |
| `GET` | `/core/settings/upgrade` | Load upgrade info |
| `POST` | `/core/settings/upgrade` | Upgrade |
| `POST` | `/core/settings/upgrade/notes` | Load release notes by version |
| `GET` | `/core/settings/upgrade/releases` | Load upgrade notes |
| `POST` | `/cronjobs/export` | Export cronjob list |
| `POST` | `/cronjobs/group/update` | Update cronjob group |
| `POST` | `/cronjobs/import` | Import cronjob list |
| `POST` | `/cronjobs/load/info` | Load cronjob info |
| `POST` | `/cronjobs/next` | Load cronjob spec time |
| `GET` | `/cronjobs/script/options` | Load script options |
| `POST` | `/cronjobs/stop` | Handle stop job |
| `GET` | `/dashboard/app/launcher` | Load app launcher |
| `POST` | `/dashboard/app/launcher/option` | Load app launcher options |
| `POST` | `/dashboard/app/launcher/show` | Update app Launcher |
| `GET` | `/dashboard/base/:ioOption/:netOption` | Load dashboard base info |
| `GET` | `/dashboard/current/:ioOption/:netOption` | Load dashboard current info |
| `GET` | `/dashboard/current/node` | Load dashboard current info for node |
| `GET` | `/dashboard/current/top/cpu` | Load top cpu processes |
| `GET` | `/dashboard/current/top/mem` | Load top memory processes |
| `POST` | `/dashboard/quick/change` | Update quick jump |
| `GET` | `/dashboard/quick/option` | Load quick jump options |
| `POST` | `/dashboard/system/restart/:operation` | System restart |
| `GET` | `/databases/db/:name` | Get databases |
| `POST` | `/databases/db/del/check` | Check before delete remote database |
| `GET` | `/databases/db/item/:type` | List databases |
| `GET` | `/databases/db/list/:type` | List databases |
| `POST` | `/databases/format/options` | List mysql database format collation options |
| `POST` | `/databases/pg/:database/load` | Load postgresql database from remote |
| `POST` | `/files/convert` | Convert file |
| `POST` | `/files/convert/log` | Convert file |
| `POST` | `/files/depth/size` | Multi file size |
| `POST` | `/files/mount` | system mount |
| `POST` | `/files/preview` | Preview file content |
| `POST` | `/files/remark` | Set file remark |
| `POST` | `/files/remarks` | Batch get file remarks |
| `POST` | `/files/user/group` | system user and group |
| `POST` | `/files/wget/stop` | Stop wget file download |
| `GET` | `/hosts/components/{name}` | Check if a system component exists |
| `GET` | `/hosts/disks` | Get complete disk information |
| `POST` | `/hosts/disks/mount` | Mount disk |
| `POST` | `/hosts/disks/partition` | Partition disk |
| `POST` | `/hosts/disks/unmount` | Unmount disk |
| `POST` | `/hosts/firewall/base` | Load firewall base info |
| `POST` | `/hosts/firewall/filter/chain/status` | load chain status with name |
| `POST` | `/hosts/firewall/filter/operate` | Apply/Unload/Init iptables filter |
| `POST` | `/hosts/firewall/filter/rule/batch` | Batch operate iptables filter rules |
| `POST` | `/hosts/firewall/filter/rule/operate` | Operate iptables filter rule |
| `POST` | `/hosts/firewall/filter/search` | search iptables filter rules |
| `POST` | `/hosts/monitor/gpu/search` | Load monitor data |
| `GET` | `/hosts/monitor/setting` | Load monitor setting |
| `POST` | `/hosts/monitor/setting/update` | Update monitor setting |
| `POST` | `/hosts/ssh/cert` | Generate host SSH secret |
| `POST` | `/hosts/ssh/cert/delete` | Delete host SSH secret |
| `POST` | `/hosts/ssh/cert/search` | Load host SSH secret |
| `POST` | `/hosts/ssh/cert/sync` | Sycn host SSH secret |
| `POST` | `/hosts/ssh/cert/update` | Update host SSH secret |
| `POST` | `/hosts/ssh/file` | Load host SSH conf |
| `POST` | `/hosts/ssh/file/update` | Update host SSH setting by file |
| `POST` | `/hosts/ssh/log/export` | Export host SSH logs |
| `POST` | `/hosts/tool/init` | Create Host tool Config |
| `GET` | `/logs/tasks/executing/count` | Get the number of executing tasks |
| `POST` | `/logs/tasks/search` | Page task logs |
| `POST` | `/openresty/build` | Build OpenResty |
| `GET` | `/openresty/https` | Get default HTTPs status |
| `POST` | `/openresty/https` | Operate default HTTPs |
| `GET` | `/openresty/modules` | Get OpenResty modules |
| `POST` | `/openresty/modules/update` | Update OpenResty module |
| `POST` | `/process/listening` | Get Listening Process |
| `GET` | `/process/{pid}` | Get Process Info By PID |
| `GET` | `/runtimes/:id` | Get runtime |
| `GET` | `/runtimes/installed/delete/check/:id` | Delete runtime |
| `GET` | `/runtimes/php/:id/extensions` | Get php runtime extension |
| `POST` | `/runtimes/php/config` | Update runtime php conf |
| `GET` | `/runtimes/php/config/:id` | Load php runtime conf |
| `GET` | `/runtimes/php/container/:id` | Get PHP container config |
| `POST` | `/runtimes/php/container/update` | Update PHP container config |
| `POST` | `/runtimes/php/extensions/install` | Install php extension |
| `POST` | `/runtimes/php/extensions/uninstall` | UnInstall php extension |
| `POST` | `/runtimes/php/file` | Get php conf file |
| `POST` | `/runtimes/php/fpm/config` | Update fpm config |
| `GET` | `/runtimes/php/fpm/config/:id` | Get fpm config |
| `GET` | `/runtimes/php/fpm/status/:id` | Get PHP runtime status |
| `POST` | `/runtimes/php/update` | Update php conf file |
| `POST` | `/runtimes/remark` | Update runtime remark |
| `POST` | `/runtimes/supervisor/process` | Operate supervisor process |
| `GET` | `/runtimes/supervisor/process/:id` | Get supervisor process |
| `POST` | `/runtimes/supervisor/process/file` | Operate supervisor process file |
| `POST` | `/settings/description/save` | Save common description |
| `GET` | `/settings/get/{key}` | Load system setting by key |
| `GET` | `/settings/snapshot/load` | Load system snapshot data |
| `POST` | `/settings/snapshot/recreate` | Recreate system snapshot |
| `POST` | `/settings/ssh` | Save local conn info |
| `POST` | `/settings/ssh/check/info` | Check local conn info |
| `GET` | `/settings/ssh/conn` | Load local conn |
| `POST` | `/settings/ssh/conn/default` | Update local is conn |
| `POST` | `/toolbox/clam/base` | Load clam base info |
| `GET` | `/toolbox/device/users` | Load user list |
| `GET` | `/websites/:id` | Search website by id |
| `GET` | `/websites/:id/config/:type` | Search website nginx by id |
| `GET` | `/websites/:id/https` | Load https conf |
| `POST` | `/websites/:id/https` | Update https conf |
| `POST` | `/websites/acme/update` | Update website acme account |
| `POST` | `/websites/auths/path` | Get AuthBasic conf |
| `POST` | `/websites/auths/path/update` | Get AuthBasic conf |
| `POST` | `/websites/batch/group` | Batch set website group |
| `POST` | `/websites/batch/https` | Batch set HTTPS for websites |
| `POST` | `/websites/batch/operate` | Batch operate websites |
| `POST` | `/websites/cors/update` | Update CORS Config |
| `GET` | `/websites/cors/{id}` | Get CORS Config |
| `POST` | `/websites/crosssite` | Operate Cross Site Access |
| `GET` | `/websites/databases` | Get databases |
| `POST` | `/websites/databases` | Change website database |
| `GET` | `/websites/default/html/:type` | Get default html |
| `GET` | `/websites/domains/:websiteId` | Search website domains by websiteId |
| `POST` | `/websites/domains/update` | Update website domain |
| `POST` | `/websites/exec/composer` | Exec Composer |
| `GET` | `/websites/lbs` | Get website upstreams |
| `POST` | `/websites/lbs/create` | Create website upstream |
| `POST` | `/websites/lbs/del` | Delete website upstream |
| `POST` | `/websites/lbs/file` | Update website upstream file |
| `POST` | `/websites/lbs/update` | Update website upstream |
| `POST` | `/websites/options` | List website names |
| `POST` | `/websites/proxies/delete` | Delete proxy config |
| `POST` | `/websites/proxies/file` | Update proxy file |
| `POST` | `/websites/proxies/status` | Update proxy config status |
| `POST` | `/websites/proxy/clear` | Clear Website proxy cache |
| `POST` | `/websites/proxy/config` | update website proxy cache config |
| `GET` | `/websites/proxy/config/{id}` | Get website proxy cache config |
| `POST` | `/websites/realip/config` | Set Real IP |
| `GET` | `/websites/realip/config/{id}` | Get Real IP Config |
| `GET` | `/websites/resource/{id}` | Get website resource |
| `GET` | `/websites/rewrite/custom` | List custom rewrite |
| `POST` | `/websites/rewrite/custom` | Operate custom rewrite |
| `GET` | `/websites/ssl/:id` | Search website ssl by id |
| `POST` | `/websites/ssl/list` | List website ssl |
| `POST` | `/websites/ssl/upload/file` | Upload SSL file |
| `GET` | `/websites/ssl/website/:websiteId` | Search website ssl by website id |
| `POST` | `/websites/stream/update` | Update Stream Config |

## Removed APIs (115)

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/ai/ollama/model/close` | Close Ollama model conn |
| `GET` | `/apps/detail/{appId}/{version}/{type}` | Search app detail by appid |
| `GET` | `/apps/details/{id}` | Get app detail by id |
| `GET` | `/apps/ignored` | Get Ignore App |
| `GET` | `/apps/installed/conninfo/{key}` | Search app password by key |
| `GET` | `/apps/installed/delete/check/{appInstallId}` | Check before delete |
| `GET` | `/apps/installed/params/{appInstallId}` | Search params by appInstallId |
| `GET` | `/apps/services/{key}` | Search app service by key |
| `POST` | `/apps/sync` | Sync app list |
| `GET` | `/apps/{key}` | Search app by key |
| `GET` | `/auth/captcha` | Load captcha |
| `GET` | `/auth/demo` | Check System isDemo |
| `GET` | `/auth/intl` | Check System isIntl |
| `GET` | `/auth/language` | Load System Language |
| `POST` | `/auth/login` | User login |
| `POST` | `/auth/logout` | User logout |
| `POST` | `/auth/mfalogin` | User login with mfa |
| `GET` | `/containers/compose/search/log` | Container Compose logs |
| `POST` | `/containers/download/log` | Download Container logs |
| `POST` | `/containers/load/log` | Load container log |
| `GET` | `/containers/repo/status` | Load repo status |
| `POST` | `/containers/search/log` | Container logs |
| `GET` | `/containers/stats/{id}` | Container stats |
| `POST` | `/cronjobs/download` | Download cronjob records |
| `GET` | `/dashboard/base/{ioOption}/{netOption}` | Load dashboard base info |
| `POST` | `/dashboard/current` | Load dashboard current info |
| `POST` | `/dashboard/system/restart/{operation}` | System restart panel |
| `GET` | `/databases/db/item/{type}` | Retrieve database list based on type |
| `GET` | `/databases/db/list/{type}` | List databases |
| `GET` | `/databases/db/{name}` | Get databases |
| `GET` | `/databases/options` | List mysql database names |
| `POST` | `/databases/pg/{database}/load` | Load postgresql database from remote |
| `POST` | `/db/remote/del/check` | Check before delete remote database |
| `POST` | `/hosts` | Create host |
| `GET` | `/hosts/command` | List commands |
| `POST` | `/hosts/command` | Create command |
| `POST` | `/hosts/command/del` | Delete command |
| `GET` | `/hosts/command/redis` | List redis commands |
| `POST` | `/hosts/command/redis` | Save redis command |
| `POST` | `/hosts/command/redis/del` | Delete redis command |
| `POST` | `/hosts/command/redis/search` | Page redis commands |
| `POST` | `/hosts/command/search` | Page commands |
| `GET` | `/hosts/command/tree` | Tree commands |
| `POST` | `/hosts/command/update` | Update command |
| `POST` | `/hosts/conffile/update` | Update host SSH setting by file |
| `POST` | `/hosts/del` | Delete host |
| `GET` | `/hosts/firewall/base` | Load firewall base info |
| `POST` | `/hosts/search` | Page host |
| `GET` | `/hosts/ssh/conf` | Load host SSH conf |
| `POST` | `/hosts/ssh/generate` | Generate host SSH secret |
| `POST` | `/hosts/ssh/secret` | Load host SSH secret |
| `POST` | `/hosts/test/byid/{id}` | Test host conn by host id |
| `POST` | `/hosts/test/byinfo` | Test host conn by info |
| `POST` | `/hosts/tool/create` | Create Host tool Config |
| `POST` | `/hosts/tool/log` | Get tool logs |
| `POST` | `/hosts/tree` | Load host tree |
| `POST` | `/hosts/update` | Update host |
| `POST` | `/hosts/update/group` | Update host group |
| `POST` | `/logs/clean` | Clean operation logs |
| `POST` | `/logs/login` | Page login logs |
| `POST` | `/logs/operation` | Page operation logs |
| `POST` | `/logs/system` | Load system logs |
| `POST` | `/openresty/clear` | Clear OpenResty proxy cache |
| `GET` | `/runtimes/{id}` | Get runtime |
| `POST` | `/settings/api/config/generate/key` | Generate api key |
| `POST` | `/settings/api/config/update` | Update api config |
| `POST` | `/settings/backup` | Create backup account |
| `POST` | `/settings/backup/backup` | Backup system data |
| `POST` | `/settings/backup/del` | Delete backup account |
| `GET` | `/settings/backup/onedrive` | Load OneDrive info |
| `POST` | `/settings/backup/record/del` | Delete backup record |
| `POST` | `/settings/backup/record/download` | Download backup record |
| `POST` | `/settings/backup/record/search` | Page backup records |
| `POST` | `/settings/backup/record/search/bycronjob` | Page backup records by cronjob |
| `POST` | `/settings/backup/record/size` | Load backup records size |
| `POST` | `/settings/backup/record/size/bycronjob` | Load backup records size for cronjob |
| `POST` | `/settings/backup/recover` | Recover system data |
| `POST` | `/settings/backup/recover/byupload` | Recover system data by upload |
| `POST` | `/settings/backup/refresh/onedrive` | Refresh OneDrive token |
| `GET` | `/settings/backup/search` | List backup accounts |
| `POST` | `/settings/backup/search` | List buckets |
| `POST` | `/settings/backup/search/files` | List files from backup accounts |
| `POST` | `/settings/backup/update` | Update backup account |
| `POST` | `/settings/bind/update` | Update system bind info |
| `POST` | `/settings/expired/handle` | Reset system password expired |
| `GET` | `/settings/interface` | Load system address |
| `POST` | `/settings/menu/update` | Update system setting |
| `POST` | `/settings/mfa` | Load mfa info |
| `POST` | `/settings/mfa/bind` | Bind mfa |
| `POST` | `/settings/password/update` | Update system password |
| `POST` | `/settings/port/update` | Update system port |
| `POST` | `/settings/proxy/update` | Update proxy setting |
| `POST` | `/settings/snapshot/size` | Load system snapshot size |
| `POST` | `/settings/snapshot/status` | Load Snapshot status |
| `POST` | `/settings/ssl/download` | Download system cert |
| `GET` | `/settings/ssl/info` | Load system cert info |
| `POST` | `/settings/ssl/update` | Update system ssl |
| `GET` | `/settings/upgrade` | Load release notes by version |
| `POST` | `/settings/upgrade` | Upgrade |
| `GET` | `/toolbox/clam/base` | Load clam base info |
| `POST` | `/toolbox/clam/record/log` | Load clam record detail |
| `GET` | `/websites/default/html/{type}` | Get default html |
| `GET` | `/websites/domains/{websiteId}` | Search website domains by websiteId |
| `GET` | `/websites/options` | List website names |
| `POST` | `/websites/php/config` | Update website php conf |
| `GET` | `/websites/php/config/{id}` | Load website php conf |
| `POST` | `/websites/php/update` | Update php conf |
| `POST` | `/websites/proxies/del` | Delete proxy conf |
| `POST` | `/websites/proxy/file` | Update proxy file |
| `GET` | `/websites/ssl/website/{websiteId}` | Search website ssl by website id |
| `GET` | `/websites/ssl/{id}` | Search website ssl by id |
| `GET` | `/websites/{id}` | Search website by id |
| `GET` | `/websites/{id}/config/{type}` | Search website nginx by id |
| `GET` | `/websites/{id}/https` | Load https conf |
| `POST` | `/websites/{id}/https` | Update https conf |

## Modified APIs (300)

| Method | Path | Changes |
|--------|------|---------|
| `POST` | `/apps/installed/ignore` | `summary`: `ignore App Update` → `Ignore Upgrade App` |
| `POST` | `/apps/installed/update/versions` | `parameters`: `0` → `1` |
| `POST` | `/containers/compose/update` | `summary`: `Update Container Compose` → `Update compose` |
| `GET` | `/containers/volume` | `summary`: `List Container Volumes` → `List volumes` | `summary`: `Create Container Volume` → `Create volume` |
| `POST` | `/containers/volume` | `summary`: `List Container Volumes` → `List volumes` | `summary`: `Create Container Volume` → `Create volume` |
| `POST` | `/containers/volume/del` | `summary`: `Delete Container Volume` → `Delete volume` |
| `POST` | `/containers/volume/search` | `summary`: `Page Container Volumes` → `Page volumes` |
| `POST` | `/databases/pg` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/bind` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/del` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/del/check` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/description` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/password` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/privileges` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/databases/pg/search` | `tags`: `['Database Postgresql']` → `['Database PostgreSQL']` |
| `POST` | `/files/chunkupload` | `summary`: `Chunk upload file` → `ChunkUpload file` |
| `POST` | `/files/recycle/clear` | `summary`: `Clear Recycle Bin files` → `Clear RecycleBin files` |
| `POST` | `/files/recycle/reduce` | `summary`: `Reduce Recycle Bin files` → `Reduce RecycleBin files` |
| `POST` | `/files/recycle/search` | `summary`: `List Recycle Bin files` → `List RecycleBin files` |
| `GET` | `/files/recycle/status` | `summary`: `Get Recycle Bin status` → `Get RecycleBin status` |
| `POST` | `/groups` | `summary`: `Create system group` → `Create group` |
| `POST` | `/groups/del` | `summary`: `Delete system group` → `Delete group` |
| `POST` | `/groups/search` | `summary`: `List system groups` → `List groups` |
| `POST` | `/groups/update` | `summary`: `Update system group` → `Update group` |
| `POST` | `/hosts/firewall/batch` | `summary`: `Batch create group` → `Batch operate rule` |
| `POST` | `/hosts/firewall/forward` | `summary`: `Update firewall port group` → `Operate forward rule` |
| `POST` | `/hosts/firewall/ip` | `summary`: `Create firewall group` → `Operate Ip rule` |
| `POST` | `/hosts/firewall/operate` | `summary`: `Page firewall status` → `Operate firewall` |
| `POST` | `/hosts/firewall/port` | `summary`: `Create firewall port group` → `Create group` |
| `POST` | `/hosts/firewall/update/addr` | `summary`: `Update address group` → `Update Ip rule` |
| `POST` | `/hosts/firewall/update/port` | `summary`: `Update firewall group` → `Update port rule` |
| `POST` | `/hosts/monitor/clean` | `summary`: `Clean monitor datas` → `Clean monitor data` |
| `POST` | `/hosts/monitor/search` | `summary`: `Load monitor datas` → `Load monitor data` |
| `POST` | `/hosts/tool/supervisor/process/file` | `summary`: `Get Supervisor process config` → `Get Supervisor process config file` |
| `GET` | `/settings/basedir` | `summary`: `Load local base dir` → `Load local backup dir` |
| `POST` | `/websites/ca/renew` | `summary`: `Renew Obtain SSL` → `Obtain SSL` |
| `POST` | `/websites/leech/update` | `summary`: `Update AntiLeech conf` → `Update AntiLeech` |
| `POST` | `/websites/ssl/download` | `summary`: `Download SSL file` → `Download SSL  file` |
| `POST` | `/websites/ssl/update` | `summary`: `Update Website ssl` → `Update ssl` |
| `POST` | `/websites/ssl/upload` | `summary`: `Upload Website ssl` → `Upload ssl` |