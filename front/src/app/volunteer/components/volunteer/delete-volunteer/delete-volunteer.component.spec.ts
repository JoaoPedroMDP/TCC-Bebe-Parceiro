import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteVolunteerComponent } from './delete-volunteer.component';

describe('DeleteVolunteerComponent', () => {
  let component: DeleteVolunteerComponent;
  let fixture: ComponentFixture<DeleteVolunteerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteVolunteerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteVolunteerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
