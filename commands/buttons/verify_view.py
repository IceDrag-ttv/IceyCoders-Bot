import nextcord

VIEW_NAME = "VerifyView"
VERIFY_ID = "942461296836759592"

class VerifyView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role = interaction.guild.get_role(942461296836759592)
        nver = interaction.guild.get_role(942461297465909318)
        assert isinstance(role, nextcord.Role)
        if role in interaction.user.roles:
            await interaction.user.add_roles(nver)
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Your {role.name} role has been removed.", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            try:
                await interaction.user.remove_roles(nver)
            except:
                return
            await interaction.response.send_message(f"You have been given the {role.name} role.", ephemeral=True)

    def custom_id(view: str, id: int) -> str:
        return f"{view}:{id}"
    
    @nextcord.ui.button(label="Verify", style=nextcord.ButtonStyle.green, custom_id='VerifyView:942461296836759592')
    async def VERIFY_button(self, button, interaction):
        await self.handle_click(button, interaction)